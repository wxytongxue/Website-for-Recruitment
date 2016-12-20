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

count=[1,2,3,4,5,6,7]
