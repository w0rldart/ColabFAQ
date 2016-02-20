# Requirements

 - [MongoDB](https://www.mongodb.com/download-center)
 - [pip](https://pip.pypa.io/en/stable/installing/)
 - [virtualenv](https://virtualenv.readthedocs.org/en/latest/installation.html)
 - [uWSGI](https://uwsgi-docs.readthedocs.org/en/latest/Install.html)
 - [python 2.7](https://www.python.org/download/releases/2.7/)
 - [uwsgi-plugin-python](http://stackoverflow.com/a/11055729/971392)

# Deployment notes

 - Create the virtual environment `virtualenv flask`
 - Activate it `source flask/bin/activate`
 - Install dependencies `pip install -r requirements/dev.txt`
 - Copy `env.py.example` to `env.py` and choose your desired environment
 - Test uWSGI serving `uwsgi --http-socket 127.0.0.1:8080 --plugin python --wsgi-file uwsgi.py --callable app --home flask --master`

For an Nginx with uWSGI environment, have a look into etc directory for config files
`uwsgi --ini uwsgi.ini`

# Development assets
 - Requirements: [npm](), [bower]() and [gulp]()
 - `npm install`
 - `bower install`
 - Build Semantic UI assets `cd vendor/semantic/ && gulp build`
 - Back to root boilerplate to build our assets `cd ../../ && gulp build`
 - List all available commands by executing `gulp help`


https://github.com/web2py/web2py/blob/master/scripts/setup-web2py-nginx-uwsgi-ubuntu.sh
