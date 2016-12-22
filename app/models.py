#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ext import db

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(80),unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(200))
    role = db.Column(db.Integer)   #1 学生  2高校  3用人单位 4政府
    def __init__(self,username,email,password,role):
        self.username=username
        self.email=email
        self.password=password
        self.role=role
    def __repr__(self):
        return '<User %r>' % self.username

class Student(db.Model):
    __tablename__='student'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    ID = db.Column(db.Integer,unique=True)   #学号
    name = db.Column(db.String(128))
    school = db.Column(db.String(128))
    school_id = db.Column(db.Integer)
    grade = db.Column(db.String(128))
    job = db.Column(db.String(128))
    def __init__(self,ID,name,school,school_id,grade,job):
        self.ID=ID
        self.name=name
        self.school=school
        self.school_id=school_id
        self.grade=grade
        self.job=job
    def __repr__(self):
        return '<User %r>' % self.name

class School(db.Model):
    __tablename__='school'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(255))
    desc = db.Column(db.Text)
    gover_id = db.Column(db.Integer)
    def __init__(self,name,address,desc,gover_id):
        self.name=name
        self.address=address
        self.desc=desc
        self.gover_id=gover_id
    def __repr__(self):
        return '<User %r>' % self.name

class Company(db.Model):
    __tablename__='company'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = Column(db.String(128))
    category = Column(db.String(128))
    nature = db.Column(db.String(128))
    count = db.Column(db.Integer)
    address = db.Column(db.String(255))
    desc = db.Column(db.Text)
    link = db.Column(db.String(255))
    __init__(self,name,category,nature,count,address,desc,link):
        self.name=name
        self.category=category
        self.nature=nature
        self.count=count
        self.address=address
        self.defc=defc
        self.link=link
    def __repr__(self):
        return '<User %r>' % self.name
class Goverment(db.Model):
    __tablename__='goverment'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = Column(db.String(128))
    address = db.Column(db.String(255))
    __init__(self,name,address):
        self.name=name
        self.address=address
    def __repr__(self):
        return '<User %r>' % self.name
