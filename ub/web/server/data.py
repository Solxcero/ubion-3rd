from flask import Flask, render_template , request

app  = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/second/')
def second():
    _id = request.args.get("id")  # "id": key 값 , _id: value값 
    _pass = request.args.get("pass")
    print(_id,_pass)
    return render_template('second.html', id=_id, _pass=_pass)

    #if _id=="asd" and _pass=="qwe":
   #    return render_template("second.html")
    #else:
     #   return "fail"

#id랑 pw입력하고 submit하면 cmd 창에 "이거 윗줄에 있음 =>GET /second/?id=asd&pass=qwe HTTP/1.1" 200 -" 확인 가능
#second 파일에 입력하는 이유: second에서 그 입력값을 받겠다는 뜻 


@app.route('/third/',methods=["POST"])  #post 형식이면 URL 치고 들어갈 수 없음 
def third():
    _id = request.form['id']
    _pass = request.form['pass']
    print(_id,_pass)
    return "Hola"
app.run