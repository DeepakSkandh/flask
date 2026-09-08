from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def home():
    x = False
    return render_template(
        "home2.html",
        x=x
    )
if __name__ == "__main__":
    app.run(debug=True,port=9999)
