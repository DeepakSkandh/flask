from flask import Flask, request, redirect

app = Flask(__name__)

users = {}   # {id: name}  e.g. {1: "Deepak", 2: "Ravi"}


# READ (all) + the "add" form
@app.route("/")
def index():
    html = "<h2>Users</h2><ul>"
    for id, name in users.items():
        html += f"""
            <li>
                {name}
                <a href="/edit/{id}">Edit</a>
                <form action="/delete/{id}" method="post" style="display:inline">
                    <button>Delete</button>
                </form>
            </li>
        """
    html += "</ul>"
    html += """
        <form action="/create" method="post">
            <input name="name" placeholder="New name">
            <button>Add</button>
        </form>
    """
    return html


# CREATE
@app.route("/create", methods=["POST"])
def create():
    new_id = max(users, default=0) + 1
    users[new_id] = request.form["name"]
    return redirect("/")


# UPDATE, step 1: show the edit form, pre-filled
@app.route("/edit/<int:id>")
def edit(id):
    if id not in users:
        return "User not found", 404
    return f"""
        <h2>Edit user {id}</h2>
        <form action="/update/{id}" method="post">
            <input name="name" value="{users[id]}">
            <button>Save</button>
        </form>
        <a href="/">Cancel</a>
    """


# UPDATE, step 2: save the change
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    if id not in users:
        return "User not found", 404
    users[id] = request.form["name"]
    return redirect("/")


# DELETE
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    users.pop(id, None)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)