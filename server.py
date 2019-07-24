from flask import Flask,request,redirect,url_for,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='192.168.100.45',port=80)
