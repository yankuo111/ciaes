#!/usr/bin/python3

# @File: sessionWork.py

# -*-coding:utf-8-*-

# @Author:Guan_pc

# @Time: 2023年03月31日11时

# 说明:

# 说明:
import time
import uuid
from math import ceil

from app.config import resStand, pageSizeSession, pageSizeChat
# from app.createApp import mysqlLink as db
# from database.tables import ChatSession, ChatRecord
# from generateModel.config import sameNodeNum
# from generateModel.knowledgeSearch.langChainSearch import searchNodes



def createSessionWork():
    sessionId = uuid.uuid1().hex
    data = {
        'sessionId': sessionId
    }
    result = resStand(0, data, '').tojson()
    return result

#
# def saveSessionWork(userId, sessionId, sessionName):
#     time_ = int(time.time())
#     if sessionName:
#         count_id = ChatSession.query.filter(ChatSession.createUserId == userId,
#                                             ChatSession.sessionId == sessionId).count()
#         count_name = ChatSession.query.filter(ChatSession.createUserId == userId,
#                                               ChatSession.sessionName == sessionName).count()
#         if count_name == 0:
#             if count_id == 0:
#                 session = ChatSession(createUserId=userId, sessionId=sessionId, sessionName=sessionName, saveTime=time_)
#                 db.session.add(session)
#                 db.session.commit()
#             else:
#                 session = ChatSession.query.filter(ChatSession.sessionId == sessionId).first()
#                 session.sessionName = sessionName
#                 db.session.commit()
#         else:
#             return resStand(3001, '', '对话名称已经存在。').tojson()
#         return resStand(0, '', 'success').tojson()
#     else:
#         return resStand(3002, '', '没有收到sessionName').tojson()
#
#
# def loadSessionWork(sessionId, page):
#     totalCount = ChatRecord.query.filter(ChatRecord.sessionId == sessionId).count()
#     data = ChatRecord.query.filter(ChatRecord.sessionId == sessionId).order_by(
#         ChatRecord.time.desc()).limit(pageSizeChat).offset(pageSizeChat * (page - 1))
#     data = [i.to_json() for i in data]
#     for i in data:
#         if i['knowledgeUsed']:
#             knowledgeIds = eval(i['knowledgeUsed'])
#             nodes = searchNodes(knowledgeIds, i['chatAsk'], topk=sameNodeNum, return_node=True)
#             i['basis'] = nodes
#     totalPage = ceil(totalCount / pageSizeChat)
#     data = {
#         "data": data,
#         "currentPage": page,
#         "pageSize": pageSizeChat,
#         "totalCount": totalCount,
#         "totalPage": totalPage
#     }
#     result = resStand(0, data, '').tojson()
#     return result
#
#
# def delSessionWork(sessionId):
#     db.session.execute(
#         f'delete FROM chatsession where sessionId = "{sessionId}"')
#     db.session.commit()
#     return resStand(0, '', 'success').tojson()
#
#
# def sessionListWork(userId, page):
#     totalCount = ChatSession.query.filter(ChatSession.createUserId == userId).count()
#     data = ChatSession.query.filter(ChatSession.createUserId == userId).order_by(
#         ChatSession.saveTime.desc()).limit(pageSizeSession).offset(pageSizeSession * (page - 1))
#     data = [i.to_json() for i in data]
#     totalPage = ceil(totalCount / pageSizeSession)
#     data = {
#         "data": data,
#         "currentPage": page,
#         "pageSize": pageSizeSession,
#         "totalCount": totalCount,
#         "totalPage": totalPage
#     }
#     result = resStand(0, data, '').tojson()
#     return result
#
#
# def searchSessionWork(userId, query):
#     sessions = ChatSession.query.filter(ChatSession.createUserId == userId,
#                                         ChatSession.sessionName.like(f'%{query}%')).limit(10)
#     sessions = [i.to_json() for i in sessions]
#     result = resStand(0, sessions, '').tojson()
#     return result

#
# if __name__ == '__main__':
#     print(loadSessionWork('76649a08d1ee11eda4e13497f65a44a7', 1))
