# -*- coding: UTF-8 -*-
"""
@Project ：ChatGLM-webui-main
@File ：glm.py
@Author ：liujiefei
@Date ：2023/3/31 17:04
"""
import os

import torch
from sentence_transformers import SentenceTransformer, util



if __name__ == '__main__':

    import pandas as pd
    # 加载SentenceTransformer模型
    model = SentenceTransformer('../sourcefile/m3e-base')

    df = pd.read_excel('output_sample.xls')
    scores_all = []
    #
    for index, row in df.iterrows():
        # 输入文本句子
        sentence1 = row.glm
        sentence2 = row["glm-int4"]
        # 编码文本句子
        embeddings1 = model.encode(sentence1, convert_to_tensor=True)
        embeddings2 = model.encode(sentence2, convert_to_tensor=True)
        # 计算余弦相似度
        cosine_similarity = util.pytorch_cos_sim(embeddings1, embeddings2)
        print(f"Cosine Similarity: {cosine_similarity.item()}")
        scores_all.append(cosine_similarity)
        df.at[index, "score"] = cosine_similarity.item()
    print(f"平均分数为：{sum(scores_all)/len(scores_all)}")
    df.to_excel('output_score.xls', index=False)

