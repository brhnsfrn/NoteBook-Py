#!/usr/bin/env python
# -- coding: utf-8 --
from functools import wraps
from flask import Response, request

def check(username, password):
    return username == 'admin' and password == 'passwd'

def authorization(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check(auth.username, auth.password):
            return Response('401 Unauthorized', 401, {'WWW-Authenticate': 'Basic realm="Access to admin area"'})
        return  f(*args, **kwargs)
    return decorated