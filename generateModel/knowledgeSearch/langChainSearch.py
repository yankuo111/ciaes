# coding: UTF-8
import os
import time

import torch
import pandas as pd
import gc
import json
from transformers import AutoTokenizer, AutoModel
from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
import numpy as np
from tqdm import tqdm
from collections import defaultdict
from generateModel.knowledgeSearch.utils import _load_vector,load_prompt_vector,list_caiwu,load_prompt_caiwu
import re
from sourcefile.config import company_path




# years = ['2019','2020','2021']


#导入公司名称
stock_mapping = json.load(open(company_path,"r"))



def trucate(question,trucate_index):
    question = question[trucate_index:]
    cleaned_text = re.sub(r'在\d{4}年|\d{4}年', '', question)
    # temp_list = cleaned_text.split("，")
    # if len(temp_list) > 1:
    #     cleaned_text = "".join(temp_list[1:])
    if '的' == cleaned_text[0]:
        cleaned_text = cleaned_text[1:]
    return cleaned_text

def trucate_opening(question,trucate_index):
    tmp_question = question.split("，")
    if len(tmp_question) == 2 and re.search("20\d{2}",tmp_question[1]):
        return tmp_question[0]
    question = question[trucate_index:]
    cleaned_text = re.sub(r'在\d{4}年|\d{4}年', '', question)
    if '的' == cleaned_text[0]:
        cleaned_text = cleaned_text[1:]
    return cleaned_text

def searchNodes(query,embeddings):
    financial_analysis = []
    if '画像' in query:
        question_type = 'image'
    elif '趋势' in query:
        question_type = 'trend'
    elif '风险' in query:
        question_type = 'risk'
    else:
        for i in list_caiwu:
            if i in query:
                financial_analysis.append(i)
        if not financial_analysis:
            question_type = 'none'
            defult_text = '请围绕企业企业画像、产业趋势、企业风险和基本财务数据查询来进行咨询，问题中应包含公司名称、年份和意图要素。\n例如：\n1.请构建2020年交控科技股份有限公司的画像。' \
                          '\n2.分析2020年交控科技股份有限公司的产业趋势。' \
                          '\n3.2020年交控科技股份有限公司的企业风险有哪些？' \
                          '\n4.交控科技股份有限公司2020年总资产是多少？'
            return question_type,defult_text
        else:
            question_type = 'caiwu'

    exist_year = False
    exist_company = False
    exist_company_list = []
    years_list = re.findall("20(?:\d{2})", query)
    if years_list:
        exist_year = True

    for stock_mapping_one in stock_mapping:
        temp_index = query.find(stock_mapping_one)
        if temp_index != -1:
            exist_company = True
            exist_company_list.append(stock_mapping_one)

    if exist_year and exist_company:

        # 去除公司及年份，截断问题
        index1 = query.find(exist_company_list[0])
        index2 = query.find('公司')
        trucate_index = max(index1 + len(exist_company_list[0]), index2 + 2)

        cleaned_text = trucate_opening(query, trucate_index)
        curret_faiss = _load_vector(exist_company_list[0], years_list[0], embeddings)
        if not curret_faiss:
            question_type = 'none'
            defult_text = '请输入正确的咨询年份（2019、2020、2021）和完整公司名称。例如：2019年交控科技股份有限公司XXXX'
            return question_type, defult_text

        if financial_analysis:
            prompt = load_prompt_caiwu(query, exist_company_list[0], years_list[0],question_type)
            if not prompt:
                question_type = 'none'
                defult_text = '无相关字段数据。'
                return question_type, defult_text

        else:
            prompt = load_prompt_vector(curret_faiss, query, cleaned_text, exist_company_list[0], years_list[0],question_type)

        print('问题是:',query)
        print(len(prompt))

        # #     # 释放缓存
        torch.cuda.empty_cache()
        gc.collect()
        return question_type,prompt
    else:
        question_type = 'none'
        defult_text = '请输入正确的咨询年份（2019、2020、2021）和完整公司名称。例如：2019年交控科技股份有限公司XXXX'
        return question_type, defult_text



# if __name__=="__main__":
#     while True:
#         question = input('请输入：')
#         # question = '分析一下宁波长阳科技股份有限公司2021年的产业趋势。'
#         answer = generate_result(question)
#         print('结果\n', answer)