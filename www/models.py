#!/usr/bin/python
#coding:utf-8

import time,uuid

from transwarp.db import next_id
from transwarp.orm import Model,StringField,BooleanField,FloatField,TextField

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    email = StringField(updateable=False,ddl="varchar(50)")
    password  = StringField(ddl="varchar(50)")
    admin = BooleanField()
    name = StringField(ddl="varchar(50)")
    image = StringField(ddl="varchar(500)")
    create_at = FloatField(updateable=False,default=time.time)


class Blog(Model):
    __table__ ='blogs'

    id = StringField(primary_key=True,default=next_id,ddl="varchar(50)")
    user_id = StringField(updateable=False,ddl="varchar(50)")
    user_name = StringField(ddl="varchar(50)")
    user_image = StringField(ddl="varchar(500)")
    name = StringField(ddl="varchar(50)")
    summary = StringField(ddl="varchar(200)")
    context = TextField()
    create_at = FloatField(updateable=False,default=time.time)


class Comment(Model):
    __table__ = "comments"

    id = StringField(primary_key=True,default=next_id,ddl="varchar(50)")
    blog_id = StringField(updateable=False,ddl="varchar(50)")
    user_id = StringField(updateable=False,ddl="varchar(50)")
    user_name = StringField(ddl="varchar(50)")
    user_image = StringField(ddl="varchar(500)")
    content = TextField()
    create_at = FloatField(updateable=False,default=time.time)


