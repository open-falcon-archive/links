# -*- coding:utf-8 -*-
__author__ = 'Ulric Qin'
from flask import request
import random
import string


def remote_ip():
    if not request.headers.getlist("X-Forward-For"):
        return request.remote_addr
    else:
        return request.headers.getlist("X-Forward-For")[0]


def random_string(length):
    s = string.lowercase + string.digits
    return ''.join(random.sample(s, length))


if __name__ == '__main__':
    print random_string(8)
    print random_string(8)