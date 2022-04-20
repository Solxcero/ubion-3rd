from flask import Flask, redirect , render_template, request, url_for
from modules import m_sql
import pandas as pd
app = Flask(__name__)


#localhost 접속
@app.route("/")
def index():
    return render_template("index.html")

#localhost/signup 로 접속
@app.route("/signup/", methods=["GET"])
def signup():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def signup_2():
    _db = m_sql.Database()   
    
    _id = request.form["_id"]
    _password = request.form["_password"]
    _name = request.form["_name"]
    _phone = request.form["_phone"]
    _gender = request.form["_gender"]
    _age = request.form["_age"]
    _ads = request.form["_ads"]
    _regitdate = request.form["_regitdate"]

    sql = '''
            INSERT INTO user_info VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
          '''
    _values = [_id,_password,_name,_phone,_ads,_gender,_age,_regitdate]
    
    _db.execute(sql,_values)
    _db.commit()
    return redirect(url_for('index'))

@app.route("/login/", methods=["POST"])
def login():
   
    _id = request.form["_id"]
    _password = request.form["_password"]
    print(_id,_password)

    sql_login = '''
                SELECT*FROM user_info 
                WHERE ID = %s AND password = %s       
                '''
                
    v = [_id,_password]
    _db = m_sql.Database()
    result = _db.executeAll(sql_login,v)
    #_db.commit()  -변경된 게 없으니까 commit no 
    
    #_db.close()
    
    print(result)
    
    if result:   # TRUE FALSE로만 /len(result) == 1
        return render_template("welcome.html", name = result[0]["name"], id = _id)   #id=result[0]["ID"]
    else:
        return redirect(url_for('index'))  #index 함수로 / redirect('/')로 해도됨/reder와 차이점:주소로 이동하는거 


@app.route("/update")  #get
def update():
    id = request.args["_id"]
    sql = '''
            SELECT*FROM user_info WHERE ID = %s
        '''
    values = [id]
    _db=m_sql.Database()
    result=_db.executeAll(sql,values)
    return render_template("update.html", info = result[0])

@app.route("/update",methods=["POST"])
def update_2():
    _id = request.form["_id"]
    _password = request.form["_password"]
    _name = request.form["_name"]
    _phone = request.form["_phone"]
    _gender = request.form["_gender"]
    _age = request.form["_age"]
    _ads = request.form["_ads"]

    sql = '''
            UPDATE user_info SET 
            password = %s,
            name =%s,
            phone = %s,
            gender = %s,
            age = %s,
            ads = %s
            WHERE ID = %s
        '''
    values = [_password, _name, _phone,_gender,_age,_ads,_id]
    _db=m_sql.Database()
    _db.execute(sql,values)
    _db.commit()
    return redirect(url_for('index'))

@app.route("/delete",methods=["GET"])
def delete():
    _id = request.args["_id"]
    return render_template("delete.html", id=_id)  #id:key . _id:value


@app.route("/delete", methods=["POST"])
def delete_2():
    _id = request.form["_id"]
    _password = request.form["_password"]
    _db=m_sql.Database()
    s_sql = '''
                SELECT*FROM user_info
                WHERE ID = %s ANd password = %s'''
    d_sql = '''
            DELETE FROM user_info
            WHERE ID = %s AND password = %s
            '''

    values = [_id,_password]
    result = _db.executeAll(s_sql, values) 

    if result :
        _db.execute(d_sql,values)  
        _db.commit()
        return redirect(url_for('index'))
    else:
        return "Wrong Password"

@app.route("/view",methods=["GET"])
def _view():
    sql = '''
          SELECT user_info.name, user_info.ads, user_info.age,
          ads_info.register_count 
          FROM user_info LEFT JOIN ads_info 
          ON user_info.ads = ads_info.ads
            '''
    _db = m_sql.Database()
    result = _db.executeAll(sql)
    key = list(result[0].keys())
    #r = pd.DataFrame(result)
    #cnt = len(r)
    return render_template("view.html",result = result, keys=key)

app.run(port=80 ,debug=True)
