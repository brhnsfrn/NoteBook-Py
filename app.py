#!/usr/bin/env python
# -- coding: utf-8 --
import datetime
from flask import Flask, make_response, redirect, render_template, request, url_for
from authenticate import authorization
from init_db import commit_db, init_db, fetch_db

app = Flask(__name__)

init_db()

@app.context_processor
def handle_context():
    return dict(title = "Notlarım", datetime = datetime, lang = "tr")

@app.route('/')
def index():
    notes = fetch_db('SELECT * FROM notes')
    return render_template('index.html', notes=notes)

@app.route('/<string:id>')
def get_by_id(id):
    notes = fetch_db('SELECT * FROM notes WHERE id=?', (id,))
    return render_template('index.html', notes=notes)

@app.route('/admin')
@authorization
def administrator():
    notes = fetch_db('SELECT * FROM notes')
    return render_template('admin.html', notes=notes)

@app.route('/admin/note/', methods=['POST'])
@authorization
def add():
    note = request.form['note']
    commit_db('INSERT INTO notes(content, created_date) VALUES(?,?)', (note, datetime.datetime.now()))
    return redirect(url_for('administrator'))

@app.route('/admin/note/<string:id>', methods=['DELETE'])
@authorization
def delete(id):
    commit_db('DELETE FROM notes WHERE id=?', (id,))
    return make_response(id, 200)


if __name__ == "__main__":
    app.secret_key = 'lUu#N}vYBW|wa.vx2idDfMapDgaUB^'
    app.run(host='0.0.0.0', port=1453, debug=True)