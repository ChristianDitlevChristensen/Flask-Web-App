from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = "5791628bb0b13ce0c676dfde280ba245"

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