# import sys, os, logging

# logging.basicConfig(stream=sys.stderr)
# sys.path.insert(0, "/var/www/otherStuff/faqcolab/")
# os.chdir("/var/www/otherStuff/faqcolab/")
# sys.path.insert(0, os.path.dirname(__file__))
# os.chdir(os.path.dirname(__file__))

# PATH = os.path.dirname(os.path.realpath(__file__))
# sys.path.insert(0, PATH)

from colabfaq import factory

app = factory.create_app()

if __name__ == "__main__":
    application.run()
