from flask import Flask,render_template
app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    return render_template("greet.html",name=name,age = 21)

if __name__ == "__main__":
    app.run(debug=True)