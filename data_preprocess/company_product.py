# coding: UTF-8
import gc
import glob

import torch
import time
import os
import json
from collections import defaultdict
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain.vectorstores import FAISS
from tqdm import tqdm
import config



text_path = config.BASE_PATH
output_path = "output"
vector_path = "output/vector"
embedding = config.EMBEDDING_MODEL


if not os.path.exists(output_path):
    os.makedirs(output_path)
if not os.path.exists(vector_path):
    os.makedirs(vector_path)

file_df = glob.glob(f"{text_path}/*.txt")

#获取公司名称
company_path = os.path.join(output_path,'company')
if not os.path.exists(company_path):
    os.makedirs(company_path)
    company_list = []
    fullname_shortname = {}
    fullname = []
    for file in os.listdir(text_path):
        company = file.split("__")[1]
        company_list.append(company)
    company_list = list(set(company_list))
    print("公司数量是",len(company_list))
    json.dump(company_list, open(f'{company_path}/company.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)

    # 创建公司简称-全称的字典
    company_year_allname = {}
    for file in os.listdir(text_path):
        company_name = file.split("__")[1]
        year = file.split("__")[4]
        company_year = company_name + "__" + year
        company_year_allname[company_year] = file
    json.dump(company_year_allname, open(f'{company_path}/company_year_allname.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)