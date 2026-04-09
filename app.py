from flask import Flask

app=Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, Welcome to Devops-Team"

@app.route("/about_us")
def about_us():
    return "About Devops-Team"

@app.route("/")
def index():
    return "Homepage of Devops-Team"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)