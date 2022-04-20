from flask import Flask, render_template, send_file  #라이브러리 check
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO



app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/corona/')
def corona():
    corona_df = pd.read_csv('corona.csv')
    corona_df.columns = ["인덱스","등록일시","사망자",
                    "확진자","게시글번호","기준일",
                    "기준시간","수정일시","누적의심자","누적확진률"]
    
    corona_df.sort_values("등록일시", inplace=True)
    corona_df["일일 사망자"] = corona_df["사망자"].diff().fillna(0)
    corona_df["일일 확진자"] = corona_df["확진자"].diff().fillna(0)

    corona_df.drop(["인덱스","게시글번호","기준일",
                                "기준시간","수정일시"],axis=1)
    corona_df.reset_index(drop = True, inplace=True) 
    corona_dict = corona_df.head(50).to_dict()
    cnt = len(corona_dict["등록일시"].keys())  # [].keys()빼면 key 갯수로 => 필요한 건 행의 갯수 (키값을 리스트로 받음=>len으로 갯수 파악)
    return render_template('corona.html', result = corona_dict,cnt=cnt) #result:키 값으로
    

   # return corona_df.to_html()

   # return corona_df.fillna(corona_df.mean()).to_html()

@app.route('/corona/des/')
def des():
    corona_df = pd.read_csv('corona.csv')
    corona_df.columns = ["인덱스","등록일시","사망자",
                    "확진자","게시글번호","기준일",
                    "기준시간","수정일시","누적의심자","누적확진률"]

    corona_des = corona_df.describe()
 
    return corona_des.to_html()
    
@app.route("/img/")
def img():
    corona_df = pd.read_csv('corona.csv')
    corona_df.columns = ["인덱스","등록일시","사망자",
                    "확진자","게시글번호","기준일",
                    "기준시간","수정일시","누적의심자","누적확진률"]
    corona_df.sort_values("등록일시", inplace=True)
    corona_df["일일 사망자"] = corona_df["사망자"].diff().fillna(0)
    decide_cnt = corona_df.head(10)["일일 사망자"].values.tolist()
    state_dt = corona_df.head(10)["등록일시"].values.tolist()

    plt.plot(state_dt,decide_cnt)
    img_1 = BytesIO()  #img_1에 BytesIO함수 불러옴 
    plt.savefig(img_1, format="png",dpi=200)
    img_1.seek(0)   

    return send_file(img_1, mimetype='image/png')

@app.route("/img2/")
def img2():
     corona_df = pd.read_csv('corona.csv')
     corona_df.columns = ["인덱스","등록일시","사망자",
                    "확진자","게시글번호","기준일",
                    "기준시간","수정일시","누적의심자","누적확진률"]
     corona_df.sort_values("등록일시", inplace=True)
     corona_df["일일 사망자"] = corona_df["사망자"].diff().fillna(0)
     corona_df["일일 확진자"] = corona_df["확진자"].diff().fillna(0)

     decide_cnt  = corona_df.head(10)["일일 확진자"].values.tolist()  #=>Series 형태를 List로 
     state_dt = corona_df.head(10)["등록일시"].values.tolist()

     plt.subplot(1,2,1)
     plt.plot(state_dt,decide_cnt)
     plt.subplot(1,2,2)
     plt.bar(state_dt,decide_cnt)
     
     img_2= BytesIO()
     plt.savefig(img_2, format='png',dpi=200)
     img_2.seek(0)

     return send_file(img_2,mimetype='image/png')

#cmd 창에 python main.py

app.run()  