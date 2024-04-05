from flask import Flask,request
# 仅包含基本程序 普通URL传输 GET方式请求
app=Flask(__name__)
@app.route('/')
def index():
    return 'test'
@app.route('/hello/<name>')
def hello(name):
    return 'hello,%s!'%name
@app.route('/lbw',methods=['GET'])
def lbw():
    name=request.args.get('name')
    hm=request.args.get('hm')
    return '你好'+name+'你的号码是'+hm
if __name__=='__main__':
    app.run(host='0.0.0.0',port='5000')
# 采用提纲上第三种方法