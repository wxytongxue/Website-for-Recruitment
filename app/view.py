#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,url_for,render_template,request,Blueprint,flash,session,redirect,g
from db import *
from form import *
from models import User,Item,Category
from ext import db

main = Blueprint('main',__name__)

@main.route('/',methods=['GET','POST'])
def index_p():
    return render_template('index.html',employment=employment,company=company,school=school)
@main.route('/login/',methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method=='POST':
        u = User.query.filter_by(email=form.email.data).first()
        if u.password == form.password.data:
            session['login']=True
            session['user']=u.username
            session['news']=2
            session['count']=[2,1,2,3,4,5,6,7]
            return render_template('index.html',employment=employment,company=company,school=school)

    session['login']=False
    return render_template('login.html',form=form)

@main.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    flash(u'登录成功，欢迎回来!')
    if request.method=='POST' and form.validate_on_submit():
        user=User(form.name.data,form.email.data,form.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html', form=form)
@main.route('/quit/')
def quit():
    session['login']=False
    session['user']=''
    return render_template('index.html',employment=employment,company=company,school=school)

# test

@main.route('/manage/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('main.complete'))

@main.route('/manage/complete/', methods=['GET', 'POST'])
def complete():
    g.complete=True
    return render_template('manage.html',completes=completes,info_email=info_email)

@main.route('/manage/verify/', methods=['GET','POST'])
def verify():
    g.verify=True
    return  render_template('manage.html',verifys=verifys,info_email=info_email)

# modify
@main.route('/manage/info-email/', methods=['GET', 'POST'])
def info_email():
    g.info_email=True
    return render_template('manage.html',information=information)

@main.route('/manage/recruit/', methods=['GET', 'POST'])
def recruit():
    g.recruit=True
    return render_template('manage.html')

@main.route('/manage/resume/', methods=['GET', 'POST'])
def resume():
    g.resume=True
    return render_template('manage.html',resumes=resumes)

@main.route('/manage/record/', methods=['GET', 'POST'])
def record():
    g.record=True
    return render_template('manage.html',records=records)

@main.route('/manage/statistics/', methods=['GET', 'POST'])
def statistics():
    g.statistics=True
    return render_template('manage.html')

@main.route('/manage/release/', methods=['GET', 'POST'])
def release():
    return render_template('manage.html')

@main.route('/job/<int:id>/',methods=['GET','POST'])
def job(id):
    return render_template('job.html')

@main.route('/school/<int:id>/',methods=['GET','POST'])
def school(id):
    return render_template('school.html')

@main.route('/company/<int:id>/',methods=['GET','POST'])
def company(id):
    return render_template('company.html') 



#the view for item
@main.route('/done/<int:id>', methods=['GET', 'POST'])
def done(id):
    return render_template('manage.html')


@main.route('/delete-item/<int:id>', methods=['GET', 'POST'])
def delete_item(id):
    return render_template('manage.html')

@main.route('/edit-item/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    return render_template('manage.html')


@main.route('/suggest/<int:id>', methods=['GET', 'POST'])
def suggest():
    return render_template('manage.html')

@main.route('/read-done/<int:id>', methods=['GET', 'POST'])
def read_done(id):
    session['news']=session['news']-1
    for s in information:
        if s['id']==id:
            information.remove(s)
    session['count'][0]=session['count'][0]-1
    return redirect(url_for('main.info_email'))
