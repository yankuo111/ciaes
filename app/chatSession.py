#!/usr/bin/python3

# @File: chatSession.py

# -*-coding:utf-8-*-

# @Author:Guan_pc

# @Time: 2023年03月30日16时

# 说明:

from flask import Blueprint, request, jsonify, g

from app.appWork.sessionWork import createSessionWork
from app.authVerify import auth

chatSession = Blueprint('chatSession', __name__)


@chatSession.route('/createSession', methods=['post'])
@auth.login_required
def createSession():
    result = createSessionWork()
    return jsonify(result)