#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ext import db

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(80),unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(200))
    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=password
    def __repr__(self):
        return '<User %r>' % self.username
