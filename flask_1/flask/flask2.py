from flask import Flask , request

app = Flask(__name__)

users = []

@app.route("/")
def home():
    return """ 
        <form action ="/register" method="post">
            <input name = "name" placeholder="Enter name">
        </form>
        <a href= "/users"> "See all users"</a> 
        
        """

@app.route("/register" ,methods=["post"])
def register():
    users.append(request.form["name"])
    print("Current users:",users)
    return 'Registered" <a href ="/"> back! </a>'

@app.route("/users")
def print_users():
    return f"users: {users}"

if __name__ == "__main__":
    app.run(debug=True)
