#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:231147@localhost/test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
manager = Manager(app)

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    def __init__(self,username,email):
        self.username=username
        self.email=email
    def __repr__(self):
        return '<User %r>' % self.username

if __name__=='__main__':
    manager.run()
