from flask import Flask,request,render_template
# GET方式请求 POST方式请求
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login',methods=['POST'])
def login():
    xm=request.form.get('xm')
    return '你好：'+xm
@app.route('/lwb',methods=['GET'])
def lwb():
    name=request.args.get('name')
    hm=request.args.get('hm')
    return '你好'+name+'你的号码是'+hm
if __name__=='__main__':
    app.run(host='0.0.0.0',port='5000')