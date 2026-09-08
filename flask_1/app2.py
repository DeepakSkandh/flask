from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Deepak"
    age = 21
    user = {
        "roll":"CB.AI.U4AIM24119",
        "role":"Student"
    }
    projects = [
    {
        "name": "Flask App",
        "description": "A web application",
        "github": "github.com/example"
    },
    {
        "name": "ML Project",
        "description": "A prediction system",
        "github": "github.com/example2"
    }
]
    return render_template(
        'home1.html',
        name=name,
        age=age,
        user=user,
        projects=projects
    )

if __name__ == "__main__":
    app.run(debug=True,port=9999)