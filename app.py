import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from function import isValid
from werkzeug.security import generate_password_hash, check_password_hash
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



@app.route("/books")
def books():
    allbooks = mongo.db.allbooks.find()
    return render_template("books.html", allbooks=allbooks)


@app.route("/all_reviews")
def all_reviews():
    all_reviews = mongo.db.tasks.find()
    return render_template("all_reviews.html",all_reviews=all_reviews)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username")
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("account.html")






if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT","5000")),
            debug=True)