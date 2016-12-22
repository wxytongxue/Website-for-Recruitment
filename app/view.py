#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,url_for,render_template,request,Blueprint,flash,session,redirect,g
from db import *
from form import *
from models import User,Student,School,Company,Goverment,Job
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
            session['role']=1
            return render_template('index.html',employment=employment,company=company,school=school)

    session['login']=False
    return render_template('login.html',form=form)

@main.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method=='POST' and form.validate_on_submit():
        user=User(form.name.data,form.email.data,form.password.data)
        db.session.add(user)
        db.session.commit()
        return render_template('info.html')
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
    return render_template('job.html',jobdesc=jobdesc,companydesc=companydesc)

@main.route('/school/<int:id>/',methods=['GET','POST'])
def school_t(id):
    return render_template('school.html',school_dis=school_dis)

@main.route('/company/<int:id>/',methods=['GET','POST'])
def company_t(id):
    return render_template('company.html',company_dis=company_dis,job_provide=job_provide)

@main.route('/info/<int:id>/',methods=['GET','POST'])
def info(id):
    return render_template('info.html')
@main.route('/edit/',methods=['GET','POST'])
def Edit():
    return render_template('edit.html')


#the view for item
@main.route('/done/<int:id>/', methods=['GET', 'POST'])
def done(id):
    return render_template('manage.html')


@main.route('/delete-item/<int:id>/', methods=['GET', 'POST'])
def delete_item(id):
    return render_template('manage.html')

@main.route('/edit-item/<int:id>/', methods=['GET', 'POST'])
def edit_item(id):
    return render_template('manage.html')


@main.route('/suggest/<int:id>', methods=['GET', 'POST'])
def suggest():
    return render_template('manage.html')

@main.route('/read-done/<int:id>/', methods=['GET', 'POST'])
def read_done(id):
    session['news']=session['news']-1
    for s in information:
        if s['id']==id:
            information.remove(s)
    session['count'][0]=session['count'][0]-1
    return redirect(url_for('main.info_email'))

@main.route('/hand-in/<int:id>/',methods=['GET','POST'])
def han_in(id):
    g.toast=True
    return render_template('job.html',jobdesc=jobdesc,companydesc=companydesc)

@main.route('/hand-info/',methods=['GET','POST'])
def hand_info():
    return render_template('index.html',employment=employment,company=company,school=school);

@main.route('/edit-info/',methods=['GET','POST'])
def edit_info():
    name=request.form.get('name')
    print name
    if name is None:
        g.empty=True
        return render_template('edit.html')
    g.empty=False
    print 'ss'
    return render_template('index.html',employment=employment,company=company,school=school);

# @main.route('/test/',methods=['GET','POST'])
# def Test():
#     return render_template('test.html')
#
# @main.route('/test-t/',methods=['GET','POST'])
# def Test_t():
#     print 'test'
#     return render_template('edit.html')
