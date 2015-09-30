import logging
from env import environment

class BaseConfig(object):
    """Base configuration."""

    def __init__(self):
        self.DEBUG = False
        self.TESTING = False
        self.BCRYPT_LOG_ROUNDS = 13

        self.SECRET_KEY = 'secretkey'
        self.WTF_CSRF_ENABLED = True
        self.LOG_LEVEL = logging.DEBUG
        self.SERVER_NAME = 'local.faqcolab.com'

        # Flask-DebugToolbar
        self.DEBUG_TB_ENABLED = False
        self.DEBUG_TB_INTERCEPT_REDIRECTS = False

        # Flask-Mail
        self.DEFAULT_MAIL_SENDER = 'Admin < username@example.com >'
        self.MAIL_SERVER = 'smtp.gmail.com'
        self.MAIL_PORT = 465
        self.MAIL_USE_SSL = True
        self.MAIL_USERNAME = 'user@example.com'
        self.MAIL_PASSWORD = '****************'

        # Flask-Security
        self.SECURITY_PASSWORD_HASH = 'sha256_crypt'
        self.SECURITY_PASSWORD_SCHEMES = ['sha256_crypt', 'django_pbkdf2_sha256']
        self.SECURITY_PASSWORD_SALT ='asgq32t1q3t2123t12t'
        self.SECURITY_EMAIL_SENDER = 'no-reply@domain.com'
        self.SECURITY_REGISTERABLE = True
        self.SECURITY_RECOVERABLE = True
        self.SECURITY_TRACKABLE = True
        self.SECURITY_CHANGEABLE = True
        self.SECURITY_LOGIN_WITHOUT_CONFIRMATION = False
        self.SECURITY_POST_REGISTER_VIEW = '/login'
        self.SECURITY_CONFIRMABLE = True

        # DB settings
        self.MONGODB_SETTINGS = {'DB': "faqColab"}


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    def __init__(self):
        super(DevelopmentConfig, self).__init__()
        self.DEBUG = True
        self.WTF_CSRF_ENABLED = False
        self.DEBUG_TB_ENABLED = True

        # Flask-Mail
        self.DEFAULT_MAIL_SENDER = 'Admin < alex@domain.com >'
        self.MAIL_SERVER = 'localhost'
        self.MAIL_PORT = 25
        self.MAIL_USE_SSL = False
        self.MAIL_USERNAME = None
        self.MAIL_PASSWORD = None

        self.MONGODB_SETTINGS = {'DB': "local_faqColab"}


class ProductionConfig(BaseConfig):
    def __init__(self):
        super(ProductionConfig, self).__init__()
        self.LOG_LEVEL = logging.INFO
        self.SERVER_NAME = 'example.com'

        self.MAIL_SERVER = 'smtp.mandrillapp.com'
        self.MAIL_PORT = 465
        self.MAIL_USE_SSL = True
        self.MAIL_USERNAME = os.getenv('MANDRILL_USERNAME')
        self.MAIL_PASSWORD = os.getenv('MANDRILL_APIKEY')

        self.MONGODB_SETTINGS = self.mongo_from_uri(os.getenv('MONGOHQ_URL'))


class TestingConfig(BaseConfig):
    """Testing configuration."""

    def __init__(self):
        super(TestingConfig, self).__init__()
        self.TESTING = True
        self.DEBUG = False
        self.BCRYPT_LOG_ROUNDS = 1
        self.WTF_CSRF_ENABLED = False

        self.MONGODB_SETTINGS = {'DB': "testing_faqColab"}


if environment == 'testing':
    app_config = TestingConfig()
elif environment == 'production':
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()