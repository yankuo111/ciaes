#!/usr/bin/python3

# @File: chat.py

# -*-coding:utf-8-*-

# @Author:Guan_pc

# @Time: 2023年03月30日15时

# 说明:

from flask import Blueprint, request, jsonify

from app.appWork.chatWork import getReplayWork, checkReplyWork, InputChat, knowledgeChatWork, testknowledgeChatWork, \
    knowledgeUsedWork, testWebChatWork
from app.authVerify import auth

chat = Blueprint('chat', __name__)


@chat.route('/reply', methods=['post'])
@auth.login_required
def reply():
    chatAsk = request.form.get('chatAsk')
    sessionId = request.form.get('sessionId')
    modelName = request.form.get('modelName')
    result = getReplayWork(sessionId, chatAsk, modelName)
    return jsonify(result)


@chat.route('/knowledgeChat', methods=['post'])
@auth.login_required
def knowledgeChat():
    query = request.form.get('query')
    knowledgeIds = request.form.get('knowledgeIds')
    sessionId = request.form.get('sessionId')
    result = knowledgeChatWork(sessionId, knowledgeIds, query)
    return jsonify(result)


@chat.route('/knowledgeUsed', methods=['post'])
@auth.login_required
def knowledgeUsed():
    knowledgeIds = request.form.get('knowledgeIds')
    query = request.form.get('query')
    result = knowledgeUsedWork(knowledgeIds, query)
    return jsonify(result)


@chat.route('/checkReply', methods=['post'])
@auth.login_required
def checkReply():
    tag = request.form.get('tag')
    chatId = request.form.get('chatId')
    result = checkReplyWork(tag, chatId)
    return jsonify(result)


@chat.route('/testInputChat', methods=['post'])
def testInputChat():
    inputText = request.form.get('inputText')
    query = request.form.get('query')
    history = request.form.get('history')
    result = InputChat(inputText, query, history)
    return jsonify(result)


@chat.route('/testknowledgeChat', methods=['post'])
def testknowledgeChat():
    query = request.form.get('query')
    history = request.form.get('history')
    knowledgeIds = request.form.get('knowledgeIds')
    result = testknowledgeChatWork(knowledgeIds, query, history)
    return jsonify(result)


@chat.route('/testWebChat', methods=['post'])
def testWebChat():
    query = request.form.get('query')
    history = request.form.get('history')
    result = testWebChatWork(query, history)
    return jsonify(result)