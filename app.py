import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from function import isValid
if os.path.exists("env.py"):
    import env

# Initilizing Flask
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Pass the Flask App to the pymongo() method
mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def homepage():
    """My Websites Homepage.
    Returns:
        renders template homepage.html
    """
    return render_template("homepage.html")


@app.route("/")
@app.route("/books")
def books():
    allbooks = mongo.db.allbooks.find()
    return render_template("books.html", allbooks=allbooks)


@app.route("/")
@app.route("/all_reviews")
def all_reviews():
    all_reviews = mongo.db.tasks.find()
    return render_template("all_reviews.html",all_reviews=all_reviews)


@app.route("/register", methods=["POST"])
def register():
    """Register an account on the website.
    URL uses a form action request on the homepage register form,
    the POST method used to get the form data is passed through the following
    validations As existing user, existing email, valid email using
    isValid() function implemented and matching passwords, if all fail then
    The form data is then inserted into the Users into the database and has encoded password
    users database along with the hashed password and the username input is set
    to session['user']
    
    Returns:Existing user =
    email =
    password=
    name=
    """
    existing_user = mongo.db.users.find_one({"user": request.form["user"]})
    existing_email = mongo.db.users.find_one({
        "email": request.form["email"]})

    if existing_user:
        flash("That username already exists! Try Again!", "error")
        return redirect(url_for("homepage"))
    if existing_email:
        flash("That email already exists! Try Again!", "error")
        return redirect(url_for("homepage"))
    if isValid(request.form["email"]) is False:
        flash("Invalid Email", "error")
        return redirect(url_for("homepage"))
    if request.form["pass"] != request.form["pass2"]:
        flash("Passwords do not match!", "error")
        return redirect(url_for("homepage"))
    hashpass = bcrypt.hashpw(
        request.form["pass"].encode("utf-8"), bcrypt.gensalt()
    )
    mongo.db.users.insert(
        {"user": request.form["user"],
         "password": hashpass,
         "email": request.form["email"],
         "profile_image": ""})
    session["user"] = request.form["user"]
    flash("Successfully Signed Up!", "success")
    return redirect(url_for("account", user=session["user"]))







if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT","5000")),
            debug=True)