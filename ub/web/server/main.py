from flask import Flask  #학습 주석 참고 

app = Flask(__name__)

@app.route('/')  #특정URL접속하면 밑의 함수 불러온다.'/':local host:5000/127.0.0.1:5000
def index():
    return "hi"

#url을 추가해서 def를 실행하려면?? 3줄만 추가 
@app.route('/second/')  #뒤에 / 적어두는 게 좋음!!=> 페이지 실행할 때 /여부 상관없이 페이지 열림 
def second():
    return "Second Page"
app.run