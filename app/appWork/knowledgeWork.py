#!/usr/bin/python3

# @File: knowledgeWork.py

# -*-coding:utf-8-*-

# @Author:Guan_pc

# @Time: 2023年04月18日15时

# 说明:

import time
from math import ceil

from bson import ObjectId
from sqlalchemy import or_, and_

from app.config import resStand, pageSizeKnowledgeTable, pageSizeKnowledgeFile
from app.createApp import mysqlLink as db
from database.config import adminId
from database.mongodb import mydb, transObjectId2Str
from database.tables import KnowledgeList
from generateModel.knowledgeSearch.langChainSearch import knowledgeManager, KnowledgeCacheLC


def createKnowledgeWork(userId, name, desc):
    createTime = int(time.time())
    count_name = KnowledgeList.query.filter(and_(KnowledgeList.createUserId == userId,
                                                 KnowledgeList.knowledgeName == name)).count()
    if len(name) > 20:
        return resStand(5001, '', '名称长度应小于20个字符。').tojson()
    if count_name:
        return resStand(5002, '', '名称已经存在。').tojson()
    else:
        row = KnowledgeList(
            createUserId=userId,
            knowledgeName=name,
            desc=desc,
            createTime=createTime
        )
        db.session.add(row)
        db.session.commit()
        row = KnowledgeList.query.filter(
            and_(KnowledgeList.createUserId == userId, KnowledgeList.knowledgeName == name)).first()
        knowledgeId = row.uniqueId
        cachelc = KnowledgeCacheLC(knowledgeId)
        knowledgeManager.set(knowledgeId, cachelc)
        return resStand(0, '', 'success').tojson()


def updateKnowledgeWork(userId, knowledgeId, name, desc):
    count_name = KnowledgeList.query.filter(and_(KnowledgeList.createUserId == userId,
                                                 KnowledgeList.knowledgeName == name)).count()
    if count_name:
        return resStand(5002, '', '名称已经存在。').tojson()
    row = KnowledgeList.query.filter(KnowledgeList.uniqueId == knowledgeId).first()
    createUser = row.createUserId
    if createUser != userId:
        return resStand(5002, '', '没有权限修改公开知识库。').tojson()
    if row:
        if name:
            if len(name) > 20:
                return resStand(5001, '', '名称长度应小于20个字符。').tojson()
            row.knowledgeName = name
        if desc:
            row.desc = desc
        db.session.commit()
        return resStand(0, '', 'success').tojson()
    else:
        return resStand(5003, '', '数据不存在。').tojson()


def deleteKnowledgeWork(userId, knowledgeId):
    count = KnowledgeList.query.filter(and_(KnowledgeList.createUserId == userId,
                                            KnowledgeList.uniqueId == knowledgeId)).count()
    if count:
        KnowledgeList.query.filter(
            and_(KnowledgeList.createUserId == userId, KnowledgeList.uniqueId == knowledgeId)).delete()
        db.session.commit()
        knowledgeManager.delete(knowledgeId)
        return resStand(0, '', 'success').tojson()
    else:
        row = KnowledgeList.query.filter(KnowledgeList.uniqueId == knowledgeId).first()
        createUser = row.createUserId
        if createUser != userId:
            return resStand(5002, '', '没有权限修改公开知识库。').tojson()
        return resStand(5003, '', '数据不存在。').tojson()


def listKnowledgeTableWork(userId, page):
    if page:
        if page.isnumeric():
            page = int(page)
        else:
            return resStand(5004, '', 'page应该是大于0的整数').tojson()
    else:
        return resStand(5004, '', '请指定页码参数：page').tojson()
    totalCount = KnowledgeList.query.filter(
        or_(KnowledgeList.createUserId == userId, KnowledgeList.createUserId == adminId)).count()
    data = KnowledgeList.query.filter(
        or_(KnowledgeList.createUserId == userId, KnowledgeList.createUserId == adminId)).order_by(
        KnowledgeList.createTime.desc(), ).limit(pageSizeKnowledgeTable).offset(pageSizeKnowledgeTable * (page - 1))
    data_ = []
    # 加入标签识别公开和私有知识库
    for row in data:
        row = row.to_json()
        if row['createUserId'] == userId:
            row['type'] = 'private'
        else:
            row['type'] = 'public'
        data_.append(row)
    totalPage = ceil(totalCount / pageSizeKnowledgeTable)
    data = {
        "data": data_,
        "currentPage": page,
        "pageSize": pageSizeKnowledgeTable,
        "totalCount": totalCount,
        "totalPage": totalPage
    }
    result = resStand(0, data, '').tojson()
    return result


def searchKnowledgeTableWork(userId, query, page):
    if page:
        if page.isnumeric():
            page = int(page)
        else:
            return resStand(5004, '', 'page应该是大于0的整数').tojson()
    else:
        return resStand(5004, '', '请指定页码参数：page').tojson()
    totalCount = KnowledgeList.query.filter(
        and_(or_(KnowledgeList.createUserId == userId, KnowledgeList.createUserId == adminId),
             KnowledgeList.knowledgeName.like(f'%{query}%'))).count()
    data = KnowledgeList.query.filter(
        and_(or_(KnowledgeList.createUserId == userId, KnowledgeList.createUserId == adminId),
             KnowledgeList.knowledgeName.like(f'%{query}%'))).order_by(
        KnowledgeList.createTime.desc()).limit(pageSizeKnowledgeTable).offset(pageSizeKnowledgeTable * (page - 1))
    data_ = []
    # 加入标签识别公开和私有知识库
    for row in data:
        row = row.to_json()
        if row['createUserId'] == userId:
            row['type'] = 'private'
        else:
            row['type'] = 'public'
        data_.append(row)
    totalPage = ceil(totalCount / pageSizeKnowledgeTable)
    data = {
        "data": data_,
        "currentPage": page,
        "pageSize": pageSizeKnowledgeTable,
        "totalCount": totalCount,
        "totalPage": totalPage
    }
    result = resStand(0, data, '').tojson()
    return result


def listKnowledgeFileWork(knowledgeId, page):
    if page:
        if page.isnumeric():
            page = int(page)
        else:
            return resStand(5004, '', 'page应该是大于0的整数').tojson()
    else:
        return resStand(5004, '', '请指定页码参数：page').tojson()
    dbName = f'knowledge{knowledgeId}'
    # dbName = 'data'
    skip = pageSizeKnowledgeFile * (page - 1)
    totalCount = mydb[dbName].count_documents({})
    data = mydb[dbName].find({}, {
        '_id': 1,
        'createTime': 1,
        'policyName': 1,
        'sourceFile': 1
    }).sort('createTime', direction=-1).limit(pageSizeKnowledgeFile).skip(skip)
    data = transObjectId2Str(list(data))
    totalPage = ceil(totalCount / pageSizeKnowledgeTable)
    data = {
        "data": data,
        "currentPage": page,
        "pageSize": pageSizeKnowledgeTable,
        "totalCount": totalCount,
        "totalPage": totalPage
    }
    result = resStand(0, data, '').tojson()
    return result


def searchKnowledgeFileWork(knowledgeId, query, page):
    if page:
        if page.isnumeric():
            page = int(page)
        else:
            return resStand(5004, '', 'page应该是大于0的整数').tojson()
    else:
        return resStand(5004, '', '请指定页码参数：page').tojson()
    dbName = f'knowledge{knowledgeId}'
    # dbName = 'data'
    skip = pageSizeKnowledgeFile * (page - 1)
    totalCount = mydb[dbName].count_documents({'policyName': {'$regex': f'{query}'}})
    data = mydb[dbName].find({'policyName': {'$regex': f'{query}'}}, {
        '_id': 1,
        'createTime': 1,
        'policyName': 1,
        'sourceFile': 1
    }).sort('createTime').limit(pageSizeKnowledgeFile).skip(skip)
    data = transObjectId2Str(list(data))
    totalPage = ceil(totalCount / pageSizeKnowledgeTable)
    data = {
        "data": data,
        "currentPage": page,
        "pageSize": pageSizeKnowledgeTable,
        "totalCount": totalCount,
        "totalPage": totalPage
    }
    return resStand(0, data, '').tojson()


def getKnowledgeFileWork(knowledgeId, fileId):
    if 'knowledge' not in knowledgeId:
        dbName = f'knowledge{knowledgeId}'
    else:
        dbName = knowledgeId
    # dbName = 'data'
    data = mydb[dbName].find_one({'_id': ObjectId(fileId)})
    data = transObjectId2Str(data)
    return resStand(0, data, '').tojson()


if __name__ == '__main__':
    createKnowledgeWork(2, '智能投研', '智能投研领域知识')
