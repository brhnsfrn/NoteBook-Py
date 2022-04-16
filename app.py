#!/usr/bin/env python
# -- coding: utf-8 --
import datetime
from flask import Flask, make_response, redirect, render_template, request, url_for
from authenticate import authorization
from init_db import init_db, get_db, query_db

app = Flask(__name__)

init_db()

@app.context_processor
def handle_context():
    return dict(datetime = datetime)

@app.route('/')
def index():
    notes = query_db('SELECT * FROM notes')
    return render_template('index.html', notes=notes)

@app.route('/<string:id>')
def get_by_id(id):
    notes = query_db('SELECT * FROM notes WHERE id=?', (id,))
    return render_template('index.html', notes=notes)

@app.route('/admin')
@authorization
def administrator():
    notes = query_db('SELECT * FROM notes')
    return render_template('admin.html', notes=notes)

@app.route('/admin/note/', methods=['POST'])
@authorization
def add():
    note = request.form['note']
    conn = get_db()
    conn.execute('INSERT INTO notes(content, created_date) VALUES(?,?)', (note, datetime.datetime.now()))
    conn.commit()
    conn.close()
    return redirect(url_for('administrator'))

@app.route('/admin/note/<string:id>', methods=['DELETE'])
@authorization
def delete(id):
    conn = get_db()
    conn.execute('DELETE FROM notes WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return make_response(id, 200)


if __name__ == "__main__":
    app.secret_key = 'lUu#N}vYBW|wa.vx2idDfMapDgaUB^'
    app.run(host='0.0.0.0', port=1453, debug=True)