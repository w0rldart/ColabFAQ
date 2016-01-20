from flask import render_template, redirect
from flask.ext.security import login_required, current_user
from faqcolab.models import Company, Event, Faq

def register_routes(app):
    @app.route('/dashboard')
    @login_required
    def dashboard():
        return render_template('dashboard/index.html',
                                title = 'Dashboard')

    # Method to update user's details
    @app.route('/user', methods=['POST'])
    @login_required
    def user():
        return redirect('/dashboard')

    @app.route('/company')
    @login_required
    def company():
        company = current_user.company

        return render_template('dashboard/company.html',
                                title = 'Company',
                                company=company)

    @app.route('/settings')
    @login_required
    def settings():
        # profile = current_user.company

        return render_template('dashboard/settings.html',
                                title = 'My settings')
