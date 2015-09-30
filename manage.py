#!/usr/bin/python

# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager
from flask.ext.script.commands import Server, Shell, ShowUrls, Clean
from flask.ext.security.script import CreateUserCommand, AddRoleCommand,\
    RemoveRoleCommand, ActivateUserCommand, DeactivateUserCommand

from app import factory
from script import ResetDB, PopulateDB

app = factory.create_app()

manager = Manager(app)
manager.add_command("shell", Shell(use_ipython=True))
manager.add_command("runserver", Server(use_reloader=True))
manager.add_command("show_urls", ShowUrls())
manager.add_command("clean", Clean())

manager.add_command("reset_db", ResetDB())
manager.add_command("populate_db", PopulateDB())

manager.add_command('create_user', CreateUserCommand())
manager.add_command('add_role', AddRoleCommand())
manager.add_command('remove_role', RemoveRoleCommand())
manager.add_command('deactivate_user', DeactivateUserCommand())
manager.add_command('activate_user', ActivateUserCommand())

# manager.add_command('run_tests', RunTests())


if __name__ == "__main__":
    manager.run()