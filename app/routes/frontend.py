from flask import render_template, redirect
from flask.ext.security import login_required, current_user
from flask.ext.security.forms import LoginForm
from flask.ext.security.utils import find_redirect

def register_routes(app):
    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('frontend/index.html',
                                title = 'Home')

    @app.route("/login", methods=["GET", "POST"])
    @app.route("/login2", methods=["GET", "POST"])
    def login():
        """For GET requests, display the login form. For POSTS, login the current user
        by processing the form."""
        form = LoginForm()

        # if form.validate_on_submit():
        #     user = User.query.get(form.email.data)
        #     if user:
        #         if bcrypt.check_password_hash(user.password, form.password.data):
        #             user.authenticated = True
        #             db.session.add(user)
        #             db.session.commit()
        #             login_user(user, remember=True)
        #             return redirect(url_for("app.panel"))

        return render_template('frontend/test.html',
                                form=form,
                                test=test,
                                test3=test3)

    @app.route("/logout", methods=["GET"])
    @login_required
    def logout():
        """Logout the current user."""
        user = current_user
        user.authenticated = False
        db.session.add(user)
        db.session.commit()
        logout_user()
        return render_template("logout.html")