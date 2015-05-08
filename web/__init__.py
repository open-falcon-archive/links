# -*- coding:utf-8 -*-
__author__ = 'Ulric Qin'

import logging
import datetime
from flask import Flask

app = Flask(__name__)
app.config.from_object("frame.config")

# config log
log_formatter = '%(asctime)s\t[%(filename)s:%(lineno)d] [%(levelname)s: %(message)s]'
log_level = logging.DEBUG if app.config['DEBUG'] else logging.WARNING
logging.basicConfig(format=log_formatter, datefmt="%Y-%m-%d %H:%M:%S", level=log_level)


@app.template_filter('fmt_time')
def fmt_time_filter(value, pattern="%Y-%m-%d %H:%M"):
    if not value:
        return ''
    return datetime.datetime.fromtimestamp(value).strftime(pattern)


@app.teardown_request
def teardown_request(exception):
    from frame.store import db

    db.commit()


@app.before_request
def before_request():
    pass


from web.controller import api