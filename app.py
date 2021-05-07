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
app.config["MONGO_URI"] = os.environ.get("MONGO_URI","mongodb://localhost")
app.secret_key= os.environ.get("SECRET_KEY")

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
    allreviews = mongo.db.allreviews.find()
    return render_template("all_reviews.html",allreviews=allreviews)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    """
        Sign up function
    """

    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for('sign_up'))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(sign_up)
        session["user"] = request.form.get("username").lower()
        return redirect(url_for('profile', username=session["user"]))

    return render_template("homepage.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    """
       Login to the Profile.
    """

    if request.method == "POST":
        # check user in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # check if user exist
        if existing_user:
            # check passowrd
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for('profile', username=session["user"]))
            else:
                flash("Incorect Username and/or Password")
                return redirect(url_for('login'))
        else:
            flash("Incorect Username and/or Password")
            return redirect(url_for('login'))

    return render_template('login_modal.html')


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("homepage"))










if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT","5000")),
            debug=True)