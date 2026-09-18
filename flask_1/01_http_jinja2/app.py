from flask import Flask,request,current_app

app = Flask(__name__)

@app.route("/")
def home():
    return "home"

@app.route("/about")
def about():
    print("Request method",request.method)
    print("Request path",request.path)
    print("Current app",current_app.name)
    return "about"

@app.route("/products")

def products():
    return "not available"

@app.route("/next")

def next():
    return "<h>come again later</h>"

@app.route("/user/<name>")

def user(name):
    return"<h1>welcome, {}!</h1>".format(name)

if __name__ == "__main__":
    app.run(debug=True,port=9999)
