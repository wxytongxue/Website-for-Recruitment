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

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    location = db.Column(db.Integer, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    location = db.Column(db.Integer, unique=True)
    items = db.relationship('Item', backref='category', lazy='dynamic')
