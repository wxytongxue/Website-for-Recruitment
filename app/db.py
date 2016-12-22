#!/usr/bin/env python
# -*- coding: utf-8 -*-

employment = []
company = []
school = []

for i in range(3):
    temp=[]
    di={'job_name':"Java 工程师",'job_desc':"1、 参与项目需求分析，负责功能模块详细设计，包括软件架构设计；2、 编写符合软件工程规范的系统分析文档及详细设计文档；3、 搭建系统服务器环境，完成系统框架和核心代码",'job_link': "www.baidu.com"}
    for j in range(3):
        temp.append(di)
    employment.append(temp)

for i in range(3):
    temp=[]
    di={'co_name':"阿里巴巴",'co_desc':"1、 参与项目需求分析，负责功能模块详细设计，包括软件架构设计；2、 编写符合软件工程规范的系统分析文档及详细设计文档；3、 搭建系统服务器环境，完成系统框架和核心代码",'co_link':"www.baidu.com",'co_img':"co_{}.jpg".format(i)}
    for j in range(3):
        temp.append(di)
    company.append(temp)

for i in range(3):
    temp=[]
    di={'sc_name':"清华大学",'sc_desc':"1、 参与项目需求分析，负责功能模块详细设计，包括软件架构设计；2、 编写符合软件工程规范的系统分析文档及详细设计文档；3、 搭建系统服务器环境，完成系统框架和核心代码",'sc_link':"www.baidu.com",'sc_img':"sc_{}.jpg".format(i)}
    for j in range(3):
        temp.append(di)
    school.append(temp)

# count=[2,1,2,3,4,5,6,7]
r1={'id':1,'info':'北京大学 12'}
r2={'id':2,'info':'清华大学 13'}
r3={'id':3,'info':'浙江大学 14'}
c1={'id':4,'info':'阿里巴巴 12'}
c2={'id':5,'info':'腾讯科技 12'}
c3={'id':6,'info':'百度科技 12'}
resumes=[]
completes=[]
verifys=[]
records=[]
verifys.append(r1)
verifys.append(r2)
verifys.append(r3)
completes.append(c1)
completes.append(c2)
completes.append(c3)
resumes.append(r1)
resumes.append(r2)
resumes.append(r3)
records.append(r1)
records.append(r2)
records.append(r3)

news=1
info_1={'id':1,'in':'pass'}
info_2={'id':2,'in':'nopass'}

information=[]
information.append(info_1)
information.append(info_2)
jobdesc={'id':'1','name':'Java工程师','salary':'30k-40k','address':'上海','record':'本科','desc':''}
companydesc={'id':'1','name':'快看公司','img':'2','category':'移动互联网','nature':'上市公司','person':'500-2000','link':'http://www.flaginfo.com.cn'}


company_dis={'id':1,'name':'快看','desc':'企业移动互联领头羊，新三板上市公司，给予员工期权激励的创新潜力股',\
'job_count':'55','res_time':'2016年12月22日'}

job_provide = []
job_add={'id':1,'name':'大数据工程师','address':'上海','pu_time':'2016.12.21','salary':'30k-40k','experience':'3年-5年',\
'record':'本科','nature':'全职','link':1}
job_provide.append(job_add)

school_dis = {'id':1,'name':'清华大学','desc':'中国TOP3大学!',\
'stu_count':'1200','res_time':'2016年12月22日'}
