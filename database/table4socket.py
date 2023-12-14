#!/usr/bin/python3

#@File: table4socket.py

#-*-coding:utf-8-*-

#@Author:Guan_pc

#@Time: 2023年04月07日16时

#说明:
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy.dialects.mysql import LONGTEXT
from werkzeug.security import generate_password_hash, check_password_hash
from database.config import mysqlurl
from app.config import secretKey, database, sqlalchemyCommitOnTearoowm, sqlalchemyEcho

app_sql = app = Flask(__name__)
app_sql.config["SQLALCHEMY_DATABASE_URI"] = f'{mysqlurl}/{database}'
app_sql.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = sqlalchemyCommitOnTearoowm
app_sql.config['SQLALCHEMY_ECHO'] = sqlalchemyEcho
app_sql.config['SECRET_KEY'] = secretKey
db = SQLAlchemy(app_sql)

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
    modelVersion = db.Column(db.String(1024))
    replyTag = db.Column(db.String(64), default='无')


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
        return InviteUsers.query.get(data['id'])