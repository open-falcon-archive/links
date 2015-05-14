# -*- coding:utf-8 -*-
__author__ = 'Ulric Qin'
from web import app
from flask import render_template, request
from frame.utils import random_string
from web.model.alert import Alert


@app.route('/api/version')
def api_version():
    return '0.0.0'


@app.route('/api/health')
def api_health():
    return 'ok'


@app.route('/<path>')
def api_home(path):
    vs = Alert.select_vs(where='path=%s', params=[path])
    sms_strings = []
    if vs:
        sms_strings = vs[0].content.split(',,')
    return render_template('index.html', **locals())


@app.route('/store', methods=['POST'])
def api_store():
    sms_strings = request.get_data()
    path = random_string(8)
    ids = Alert.column('id', where='path=%s', params=[path])
    if ids:
        Alert.update_dict({'content': sms_strings}, where='id=%s', params=[ids[0]])
    else:
        Alert.insert({'path': path, 'content': sms_strings})

    return path