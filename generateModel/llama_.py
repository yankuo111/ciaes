#!/usr/bin/python3

# @File: llama_.py

# -*-coding:utf-8-*-

# @Author:Guan_pc

# @Time: 2023年03月30日17时

# 说明:

import time


class Model_eg():
    def __init__(self):
        self.model = None
        self.history_round = 20
        self.version = '测试版假模型'

    def stream_chat_(self, history, query):
        for i in '无法回答，中文llama模型部署中...':
            time.sleep(0.3)
            yield 0, i


model = Model_eg()
