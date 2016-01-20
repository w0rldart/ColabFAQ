#################
#### imports ####
#################

from flask import Flask, render_template
from flask.ext.security import Security

from flask_mail import Mail

from faqcolab.models import db, user_datastore
from faqcolab.routes.frontend import register_routes as register_frontend_routes
from faqcolab.routes.dashboard import register_routes as register_dashboard_routes
from faqcolab.forms.user import ExtendedLoginForm, ExtendedRegisterForm

# from flask.ext.debugtoolbar import DebugToolbarExtension

def create_app():
    app = Flask(__name__)

    # load configuration
    app.config.from_object('faqcolab.config.app_config')

    db.init_app(app)
    # toolbar  = DebugToolbarExtension(app)

    security = Security()
    security.init_app(
        app,
        user_datastore,
        login_form=ExtendedLoginForm,
        confirm_register_form=ExtendedRegisterForm,
        register_form=ExtendedRegisterForm
    )

    mail = Mail()
    mail.init_app(app)

    register_frontend_routes(app)
    register_dashboard_routes(app)


    ########################
    #### error handlers ####
    ########################

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template('errors/403.html'), 403


    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html'), 404


    @app.errorhandler(500)
    def server_error_page(error):
        return render_template('errors/500.html'), 500

    return app
