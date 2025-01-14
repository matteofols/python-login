from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "test_python_login"

users ={
    "tester101": "mypass101"
}

@app.route("/")
def home():
    # Checks to see if a user is currently logged
    if "username" in session:
        # If they are currently logged in, they'll go to the home page
        return render_template("home.html", username=session["username"])
    else:
        return redirect(url_for("login"))
    

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        # Grab the form data from the request object
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("home"))
        elif username in users and users[username] != password:
            error_msg = "Please enter the right password"
            return render_template("login.html", error = error_msg)
        else:
            error_msg = "Invalid credentials. PLease verify and try again"
            return render_template("login.html", error=error_msg)
    return render_template("login.html")

def signup():
    if request.method == "POST":
        # Grab the form data from the request object
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            error_msg = "username already exists. Please pick a different username"
            return render_template("signup.html", error=error_msg)
        else:
            users[username] = password

            session["username"]= username
            return redirect(url_for("home"))
        
    return render_template("signup.html")
        

        
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))



if __name__ == "main":
    app.run(debug=True)
