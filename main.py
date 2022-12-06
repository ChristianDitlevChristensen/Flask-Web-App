from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "5791628bb0b13ce0c676dfde280ba245"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://site.db"
db = SQLAlchemy(app)

class User(db.Model):
    iD = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    imageFile = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.emaile}', '{self.imageFile}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    datePosted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Colum(db.Text, nullable=False)
    userID = db.Column(db.Integer, db.Foreignkey("user.iD"), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.datePosted}')"

posts = [
    {
        "author": "Hubert Hubertsen",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "November 22, 2022"
    },
    {
        "author": "Lass Lassen",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "November 22, 2022"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'succes')
        return redirect(url_for("home"))
    else:
        return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("Hou have been logged in", "succes")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check username and password", "danger")
    else:
        return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)