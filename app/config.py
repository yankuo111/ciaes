#!/usr/bin/python3

# @File: config.py

# -*-coding:utf-8-*-

# @Author:Guan_pc

# @Time: 2023年03月30日15时

# 说明:
import os
from typing import Union

database = 'llm_chat'
sqlalchemyCommitOnTearoowm = True
sqlalchemyEcho = True
secretKey = '\xe1\xc2\xc3z\xc1\x85\xab\xcc\x82r\xa8Q\x93\xdaRqR\xdeh\xca9\xfd\x9cm'  ##加密配置
rootDir = os.path.realpath(__file__ + '/..')
logDir = os.path.join(rootDir, r'../cache/logs/app.log')
logDir = os.path.normpath(logDir)
cacheUpload = os.path.normpath(os.path.join(rootDir, r'../cache/uploadFile'))
cacheDownload = os.path.normpath(os.path.join(rootDir, r'../cache/downloadFile'))
supportFile = ('doc', 'docx', 'wps')

tokenExpiresIn = 3600 * 24
pageSizeChat = 8
pageSizeSession = 10
pageSizeKnowledgeTable = 10
pageSizeKnowledgeFile = 10
# socketIp = '10.1.139.146'
# socketPort = 21350
socketIp = '10.1.139.147'  # 或者使用字符串 'localhost'
socketPort = 21350  # 选择一个不与其他服务冲突的端口号
MainUser = [2]


class resStand():
    def __init__(self, code, data, msg):
        self.data = data
        self.code = code
        self.msg = msg

    def tojson(self):
        return {'code': self.code, 'data': self.data, 'msg': self.msg}
