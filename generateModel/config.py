#!/usr/bin/python3

#@File: config.py

#-*-coding:utf-8-*-

#@Author:Guan_pc

#@Time: 2023年04月12日09时

#说明:
import os

minBM25Score = 0
minEditScore = 2
minBertScore = 0.4

keyWordNum = 50

samePolicyNum = 10
sameNodeNum = 5
knowledgeMaxLen = 4000
sentenceLen = 400
sentenceLenStd = 200
rootDir = os.path.realpath(__file__ + '/..')
knowledgeCachePath = os.path.normpath(os.path.join(rootDir,'../cache/knowledgeLocal'))
if not os.path.isdir(knowledgeCachePath):
    os.makedirs(knowledgeCachePath)