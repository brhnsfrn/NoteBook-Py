#!/usr/bin/env python
# -- coding: utf-8 --

import datetime
from json import dump, dumps
import os
import uuid
from flask import Flask, make_response, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from authenticate import authorization

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'notes.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.context_processor
def handle_context():
    return dict(title = "Notlarım", datetime = datetime, lang = "tr")

@app.route('/')
def index():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@app.route('/<string:id>')
def get_by_id(id):
    notes = Note.query.filter_by(id = id).all()
    return render_template('index.html', notes=notes)

@app.route('/admin')
@authorization
def administrator():
    notes = Note.query.all()
    return render_template('admin.html', notes=notes)

@app.route('/admin/note/', methods=['POST'])
@authorization
def add():
    note = request.form['note']
    newNote = Note(content = note)
    db.session.add(newNote)
    db.session.commit()
    return redirect(url_for('administrator'))

@app.route('/admin/note/<string:id>', methods=['DELETE'])
@authorization
def delete(id):
    Note.query.filter_by(id = id).delete()
    db.session.commit()
    return make_response(id, 200)

class Note(db.Model):
    id = db.Column(db.String, primary_key=True, default = str(uuid.uuid4()))
    content =  db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

if __name__ == "__main__":
    db.create_all()
    app.secret_key = 'lUu#N}vYBW|wa.vx2idDfMapDgaUB^'
    app.run(host='0.0.0.0', port=1453, debug=True)