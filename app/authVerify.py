#!/usr/bin/python3

# @File: authVerify.py

# -*-coding:utf-8-*-

# @Author:Guan_pc

# @Time: 2023年03月30日16时

# 说明:

# 说明:
import time

from flask import Blueprint, request, jsonify
from flask import g
from flask_httpauth import HTTPBasicAuth

from app.config import tokenExpiresIn, resStand, MainUser
# from app.createApp import mysqlLink as db
# from database.tables import InviteUsers

verify = Blueprint('verify', __name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(self, fun):
    if request.method == 'POST':
        username_token = request.form.get('token')
    else:
        username_token = request.args.get('token')
    if not username_token:
        return False
    # user = InviteUsers.verify_auth_token(username_token)
    # if user == '':
    #     return False
    # else:
    # g.currnet_user = user
    # time_ = int(time.time())
    # if time_ > user.dueTime:
    #     return False
    # elif user.legalToken != username_token:
    #     return False
    # else:
    g.token_used = True
    return True


@auth.error_handler
def auth_error(status):
    if request.method == 'POST':
        username_token = request.form.get('token')
    else:
        username_token = request.args.get('token')
    if not username_token:
        result = resStand(1005, '', '未收到Token').tojson()
        return jsonify(result)
    try:
        user = g.currnet_user
        time_ = int(time.time())
        if time_ > user.dueTime:
            result = resStand(1003, '', '邀请码过期，请联系管理员延期。').tojson()
            return jsonify(result)
        elif user.legalToken != username_token:
            result = resStand(1004, '', '当前用户在其他客户端登录，请重新登陆！').tojson()
            return jsonify(result)
    except:
        result = resStand(1002, '', 'Token没有权限！').tojson()
        return jsonify(result)


# def workLogin(password):
#     user = InviteUsers.query.filter(InviteUsers.userName == password).first()
#     if user == None:
#         result = resStand(1001, '', '邀请码无效').tojson()
#         return result
#     if user.verify_password(password):
#         g.currnet_user = user
#         token = user.generate_auth_token(expiration=tokenExpiresIn)
#         user.legalToken = token
#         db.session.commit()
#         result = {
#             'token': token,
#             'userId': user.uniqueId,
#             'createTime': user.createTime,
#             'dueTime': user.dueTime,
#             'role': 'Admin' if user.uniqueId in MainUser else 'User'
#         }
#         result = resStand(0, result, '').tojson()
#         return result
#     else:
#         result = resStand(1001, '', '邀请码无效').tojson()
#         return result


@verify.route('/verifyPassword', methods=['post'])
def verifyPassword():
    # password = request.form.get('password')
    # result = workLogin(password)
    tmp_result = {'code': 0, 'data': {'token': 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTY5NzA4NDQzMywiZXhwIjoxNjk3MTcwODMzfQ.eyJpZCI6MTh9.l4V7PsNiSjTYmNZIwsXg_xKDwvecv8IjluV1nF-HJlCSxhD_UIfmGycMs-Dpd0t3a_7Dc87N4kjCqZqwNA1G0w', 'userId': 18, 'createTime': 1680746401, 'dueTime': 1735488000, 'role': 'Admin'}, 'msg': ''}
    return jsonify(tmp_result)
