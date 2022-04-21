#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ast import arg
import sqlite3

DATABASE = 'database.db'

def init_db():
    with sqlite3.connect(DATABASE) as database:
        db = database.cursor()
        with open('schema.sql', 'r') as f:
            db.executescript(f.read())
        database.commit()

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
     
def fetch_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def commit_db(query, args=()):
    conn = get_db()
    conn.execute(query, args)
    conn.commit()
    conn.close()
