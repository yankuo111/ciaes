#!/usr/bin/python3

# @File: chatWork.py

# -*-coding:utf-8-*-

# @Author:Guan_pc

# @Time: 2023年03月30日17时

# 说明:
import asyncio
import time

import websockets
import sys
# from app.config import resStand, socketIp, socketPort
# from app.createApp import mysqlLink as db
# from database.tables import ChatRecord, InviteUsers
# from generateModel.config import sameNodeNum
from generateModel.glm import Model_eg_glm
# from generateModel.knowledgeSearch.langChainSearch import searchNodes
from generateModel.llama_ import Model_eg


str2Model = {
    'llama': Model_eg(),
    'chatglm': Model_eg_glm(),
}

async def getReplayWorkWS(websocket, modelName='chatglm'):
    data = await websocket.recv()
    data = eval(data)
    # token = data['token']
    chatAsk = data['chatAsk']
    # sessionId = data['sessionId']
    knowledgeIds = data.get('knowledgeIds')
    knowledgeUse = True
    if modelName == None:
        modelName = 'chatglm'
    time_ = int(time.time())
    model = str2Model.get(modelName)
    history = None
    replay = model.stream_chat_(chatAsk, history=history, knowledges=knowledgeIds, knowledgeUse=knowledgeUse)
    replay_ = ''
    try:
        for qsk, rep in replay:

            #gpu模型
            new_token = rep[len(replay_):]
            replay_ = rep

            # #cpu模型
            # new_token = rep

            replayStep = {
                'isFinash': 0,
                'data': new_token
            }
            # result = resStand(0, replayStep, '').tojson()
            await websocket.send(str(replayStep))
    except:
        data = {
            'isFinash': 0,
            'data': '系统过于繁忙，我们正在努力改善，请稍后访问。'
        }
        # result = resStand(0, data, '').tojson()
        await websocket.send(str(data))



async def main():
    async with websockets.serve(getReplayWorkWS, '10.1.139.147', '6061'):
        await asyncio.Future()



if __name__ == '__main__':
    asyncio.run(main())
    # checkReplyWork(chatId='1', tag='bad')
    # a = 1
    import pandas as pd
    from tqdm import tqdm