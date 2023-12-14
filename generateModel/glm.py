# -*- coding: UTF-8 -*-
"""
@Project ：ChatGLM-webui-main
@File ：glm.py
@Author ：liujiefei
@Date ：2023/3/31 17:04
"""
import os

import torch
import chatglm_cpp
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from torch.cuda import get_device_properties
from transformers import AutoModel, AutoTokenizer, AutoConfig
# os.environ["CUDA_VISIBLE_DEVICES"]='0'
from generateModel.config import sameNodeNum, knowledgeMaxLen
from generateModel.knowledgeSearch.langChainSearch import searchNodes

from sourcefile.config import chatGLM, embedding_name, PtuningPath, vs_path,ggml
import time

class Model_eg_glm():
    def __init__(self):
        self.max_length = 3000
        self.max_context_length = 800
        self.top_p = 0.7
        self.temperature = 0.1
        self.history_round = 4
        self.version = 'chatGLM-增强对input_text的解读'
        #使用官方量化模型gpu推理
        self.tokenizer = AutoTokenizer.from_pretrained(chatGLM, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(chatGLM,trust_remote_code=True)
        self.use_cpu = False if torch.cuda.is_available() else True
        self.prepare_model()

        # # #使用ggml量化模型
        # self.pipeline = chatglm_cpp.Pipeline(ggml)

        self.precision = None
        self.init_knowledge_embedding()

    def prepare_model(self):
        if self.use_cpu:
            if self.precision == "fp32":
                self.model = self.model.float()
                self.model = self.model.float()
            elif self.precision == "bf16":
                self.model = self.model.bfloat16()
            else:
                self.model = self.model.float()
        else:
            total_vram_in_gb = get_device_properties(0).total_memory / 1e9
            print(f'GPU memory: {total_vram_in_gb:.2f} GB')

            if total_vram_in_gb > 30:
                precision = 'fp32'
            elif total_vram_in_gb > 13:
                precision = 'fp16'
            elif total_vram_in_gb > 10:
                precision = 'int8'
            else:
                precision = 'int4'

            print(f'Choosing precision {precision} according to your VRAM.'
                  f' If you want to decide precision yourself,'
                  f' please add argument --precision when launching the application.')

            if precision == "fp16":
                self.model = self.model.half().cuda()
            elif precision == "int4":
                self.model = self.model.half().quantize(4).cuda()
            elif precision == "int8":
                self.model = self.model.half().quantize(8).cuda()
            elif precision == "fp32":
                self.model = self.model.float()
        self.model.eval()

    def init_knowledge_embedding(self):
        self.embeddings = HuggingFaceEmbeddings(model_name=embedding_name)
        # self.vector_store = FAISS.load_local(vs_path, embeddings)


    def stream_chat_(self, query, history=None, knowledges=None, input_text=None, useWeb=False, knowledgeUse=False):
        try:
            question_type, input_ = searchNodes(query,self.embeddings)
            print(question_type,input_)
            if question_type == 'none':
                yield query, input_
            else:
                # for output in self.pipeline.stream_chat([input_],top_p=self.top_p,temperature=self.temperature,do_sample=False):
                #     yield query,output

                for output, history in self.model.stream_chat(
                        self.tokenizer, query=input_, history=[],
                        max_length=self.max_length,
                        top_p=self.top_p,
                        temperature=self.temperature
                ):
                    yield query, output
        except:
            torch.cuda.empty_cache()
        finally:
            torch.cuda.empty_cache()


if __name__ == '__main__':
    import time
    model = Model_eg_glm()
    t = time.time()
    query = input("请输入你的问题:")
    out = model.stream_chat_(history=None, query='中科创达软件股份有限公司2019的总资产是多少元。')
    print(time.time() - t)
    print(list(out))
