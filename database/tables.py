#!/usr/bin/python3

# @File: tables.py

# -*-coding:utf-8-*-

# @Author:Guan_pc

# @Time: 2023年03月30日15时

import random
# 说明:
import time

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy.dialects.mysql import LONGTEXT
from werkzeug.security import generate_password_hash, check_password_hash

from app.config import secretKey
from app.createApp import mysqlLink as db
from database.config import passwordlist


class EntityBase(object):

    def to_json(self):
        fields = self.__dict__
        if "_sa_instance_state" in fields:
            del fields["_sa_instance_state"]
        return fields


class ChatRecord(db.Model, EntityBase):
    __tablename__ = "chatrecord"
    __table_args__ = {"mysql_charset": "utf8"}
    uniqueId = db.Column(db.Integer, primary_key=True)
    sessionId = db.Column(db.String(512))
    time = db.Column(db.Integer)
    chatAsk = db.Column(LONGTEXT)
    modelReply = db.Column(LONGTEXT)
    knowledgeUsed = db.Column(db.String(1024), default='')
    modelVersion = db.Column(db.String(1024))
    replyTag = db.Column(db.String(64), default='无')


class ChatSession(db.Model, EntityBase):
    __tablename__ = "chatsession"
    __table_args__ = {"mysql_charset": "utf8"}
    uniqueId = db.Column(db.Integer, primary_key=True)
    createUserId = db.Column(db.Integer)
    sessionName = db.Column(db.String(1024), unique=True)
    sessionId = db.Column(db.String(512))
    saveTime = db.Column(db.Integer)


class InviteUsers(db.Model, EntityBase):
    __tablename__ = "users"
    __table_args__ = {"mysql_charset": "utf8"}
    uniqueId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(512))
    password = db.Column(db.String(512))
    createTime = db.Column(db.Integer)
    legalToken = db.Column(db.String(4096))
    dueTime = db.Column(db.Integer)

    @property
    def password_get(self):
        raise AttributeError('password is not a readable attribute')

    @password_get.setter
    def password_get(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def generate_auth_token(self, expiration):
        s = Serializer(secretKey, expires_in=expiration)
        return s.dumps({'id': self.uniqueId}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(secretKey)
        try:
            data = s.loads(token)
        except:
            return ''
        db.session.commit()
        user = db.session.query(InviteUsers).filter(InviteUsers.uniqueId == data['id']).first()
        return user


class KnowledgeList(db.Model, EntityBase):
    __tablename__ = "knowledgelist"
    __table_args__ = {"mysql_charset": "utf8"}
    uniqueId = db.Column(db.Integer, primary_key=True)
    createUserId = db.Column(db.Integer)
    knowledgeName = db.Column(db.String(512))
    desc = db.Column(LONGTEXT)
    createTime = db.Column(db.Integer)


def create_user():
    password_ = ''.join(random.sample(list(passwordlist), 16))
    createTime = int(time.time())
    password = generate_password_hash(password_)
    dueTime = createTime + 3600 * 24 * 30
    user = InviteUsers(userName=password_, password=password, createTime=createTime, dueTime=dueTime)
    db.session.add(user)
    db.session.commit()
    print('邀请码', password_)
    return password_


def change_dueTime(password, dueData):
    user = InviteUsers.query.filter(InviteUsers.userName == password).first()
    if user:
        timeArray = time.strptime(dueData, "%Y-%m-%d")
        timeStamp = int(time.mktime(timeArray))
        user.dueTime = timeStamp
        db.session.commit()
        print('ok!')
    else:
        print('用户不存在！')


db.create_all()
if __name__ == '__main__':
    import pandas as pd

    #
    # passwords = []
    # for i in range(30):
    #     password = create_user()
    #     passwords.append(password)
    # table = pd.DataFrame({'InviteCode': passwords})
    # table.to_excel('InviteCode.xlsx')

    # change_dueTime('@lZ7jaDA%58PGyvM', '2030-7-1')
    data = pd.read_excel('InviteCode.xlsx')
    for code in data['InviteCode']:
        change_dueTime(code, '2023-7-1')
