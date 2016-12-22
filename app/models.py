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
    stu_id = db.Column(db.Integer,unique=True)   #学号
    name = db.Column(db.String(128))
    school = db.Column(db.String(128))
    school_id = db.Column(db.Integer)
    grade = db.Column(db.String(128))
    job = db.Column(db.String(128))
    res_time = db.Column(db.Date)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    def __init__(self,ID,name,school,school_id,grade,job,res_time,user_id):
        self.ID=ID
        self.name=name
        self.school=school
        self.school_id=school_id
        self.grade=grade
        self.job=job
        self.res_time=res_time
        self.user_id=user_id
    def __repr__(self):
        return '<User %r>' % self.name

class School(db.Model):
    __tablename__='school'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(255))
    desc = db.Column(db.Text)
    gover_id = db.Column(db.Integer)
    img = db.Column(db.Integer)
    res_time = db.Column(db.Date)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    def __init__(self,name,address,desc,gover_id,img,res_time,user_id):
        self.name=name
        self.address=address
        self.desc=desc
        self.gover_id=gover_id
        self.img=img
        self.res_time=res_time
        self.user_id=user_id
    def __repr__(self):
        return '<User %r>' % self.name

class Company(db.Model):
    __tablename__='company'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(128))
    category = db.Column(db.String(128))
    nature = db.Column(db.String(128))
    count = db.Column(db.Integer)
    address = db.Column(db.String(255))
    desc = db.Column(db.Text)
    link = db.Column(db.String(255))
    img = db.Column(db.Integer)
    res_time = db.Column(db.Date)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    def __init__(self,name,category,nature,count,address,desc,link,img,res_time,user_id):
        self.name=name
        self.category=category
        self.nature=nature
        self.count=count
        self.address=address
        self.defc=defc
        self.link=link
        self.img=img
        self.res_time=res_time
        self.user_id=user_id
    def __repr__(self):
        return '<User %r>' % self.name
class Goverment(db.Model):
    __tablename__='goverment'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(255))
    img = db.Column(db.Integer)
    res_time = db.Column(db.Date)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    def __init__(self,name,address,img,res_time,user_id):
        self.name=name
        self.address=address
        self.img=img
        self.res_time
        self.user_id=user_id
    def __repr__(self):
        return '<User %r>' % self.name

class Job(db.Model):
    __tablename__='job'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(255))
    salary = db.Column(db.Float)
    record = db.Column(db.String(128))
    desc = db.Column(db.Text)
    experience = db.Column(db.String(128))
    nature = db.Column(db.String(128))
    pu_time = db.Column(db.Date)
    def __init__(self,name,address,salary,record,desc,experience,nature,pu_time):
        self.name=name
        self.address=address
        self.salary=salary
        self.record=record
        self.desc=desc
        self.experience=experience
        self.nature=nature
        self.pu_time=pu_time
    def __repr__(self):
        return '<User %r>' % self.name
