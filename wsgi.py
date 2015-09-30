import sys, os, logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/otherStuff/faqColab/")
# os.chdir("/var/www/otherStuff/faqColab/")
# sys.path.insert(0, os.path.dirname(__file__))
# os.chdir(os.path.dirname(__file__))

from app import factory

application = factory.create_app()

if __name__ == "__main__":
    application.run()