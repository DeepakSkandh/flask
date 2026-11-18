from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Deepak"

@app.route("/about")
def about():
    return "<h1>About the page</h1><p>Learning the flask</p>"

@app.route("/user/<name>")
def user(name):
    return f"Hi {name}"

@app.route("/square/<int:n>")
def square(n):
    return f"square of {n} is {n*n}"

if __name__ == "__main__":
    app.run(debug=True)