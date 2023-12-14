# coding: UTF-8
import pandas as pd
from generateModel.knowledgeSearch.vector_load_opening import covert_data_vector_opening
from sourcefile.config import excel_data_path

base_information = ['公司名称','注册地址','公司网址','法定代表人','职工总数']
df = pd.read_excel(excel_data_path, engine='openpyxl')
list_caiwu = [
    '货币资金','其他流动资产','流动资产合计','其他非流动金融资产', '固定资产', '在建工程',
    '无形资产','开发支出', '商誉', '长期待摊费用', '递延所得税资产', '其他非流动资产','非流动资产合计','资产总计','应付职工薪酬',
    '应交税费', '其他应付款', '应付利息', '应付股利', '应付手续费及佣金', '应付分保账款',
    '其他流动负债', '流动负债合计','其他非流动负债', '非流动负债合计', '负债合计',
    '股本', '实收资本','营业总收入', '营业收入', '利息收入',
    '营业总成本', '营业成本', '利息支出','销售费用', '管理费用', '研发费用',
    '财务费用', '利息费用', '其他收益','投资收益','营业利润', '营业外收入',
    '营业外支出', '利润总额','净利润','总资产','总负债','流动负债合计','非流动负债合计','流动资产','非流动资产']

def is_numeric(s):
    try:
        float(s)  # 尝试将字符串转换为浮点数
        return True
    except ValueError:
        return False

def product_prompt_base(company,year):
    prompt = ''
    try:
        sub_data = df[(df['公司名称'] == company) & (df['年份'] == int(year))]
        #公司基本信息构建
        for index,i in enumerate(base_information):
            value = sub_data.iloc[0][i]
            if i != "职工总数":
                if isinstance(value, str) and value != '无':
                    prompt += f"{i}是{value}；"

            else:
                if (isinstance(value, str) or isinstance(value, int)) and value != '无':
                    prompt += f"{i}是{value}。"
    except Exception as e:
        print(e)
    return prompt

def product_prompt_property(company,year):
    prompt = ''
    try:
        sub_data = df[(df['公司名称'] == company) & (df['年份'] == int(year))]

        #资产模板构建
        zichan = sub_data.iloc[0]['资产总计']
        floating_zichan = sub_data.iloc[0]['流动资产合计']
        no_floating_zichan = sub_data.iloc[0]['非流动资产合计']
        prompt_list1 = []
        if isinstance(zichan, str):
            zichan = zichan.replace(",",'')
            if is_numeric(zichan):
                prompt_tmp = f'企业总资产为{zichan}元；'
                prompt_list1.append(prompt_tmp)
        if isinstance(floating_zichan, str):
            floating_zichan = floating_zichan.replace(",",'')
            if is_numeric(floating_zichan):
                prompt_tmp = f'企业流动资产为{floating_zichan}元；'
                prompt_list1.append(prompt_tmp)

        if isinstance(no_floating_zichan, str):
            no_floating_zichan = no_floating_zichan.replace(",",'')
            if is_numeric(no_floating_zichan):
                prompt_tmp = f'企业非流动资产为{no_floating_zichan}元。\n'
                prompt_list1.append(prompt_tmp)
        if prompt_list1:
            prompt_tmp = '企业资产部分：' + ''.join(prompt_list1)
            prompt += prompt_tmp

        #负债模板构建
        fuzhai = sub_data.iloc[0]['负债合计']
        floating_fuzhai = sub_data.iloc[0]['流动负债合计']
        no_floating_fuzhai = sub_data.iloc[0]['非流动负债合计']
        prompt_list2 = []
        if isinstance(fuzhai, str):
            fuzhai = fuzhai.replace(",",'')
            if is_numeric(fuzhai):
                prompt_tmp = f'企业总负债为{fuzhai}元；'
                prompt_list2.append(prompt_tmp)
        if isinstance(floating_fuzhai, str):
            floating_fuzhai = floating_fuzhai.replace(",",'')
            if is_numeric(floating_fuzhai):
                prompt_tmp = f'企业流动负债为{floating_fuzhai}元；'
                prompt_list2.append(prompt_tmp)

        if isinstance(no_floating_fuzhai, str):
            no_floating_fuzhai = no_floating_fuzhai.replace(",",'')
            if is_numeric(no_floating_fuzhai):
                prompt_tmp = f'企业非流动负债为{no_floating_fuzhai}元。\n'
                prompt_list2.append(prompt_tmp)
        if prompt_list2:
            prompt_tmp = '企业负债部分：' + ''.join(prompt_list2)
            prompt += prompt_tmp

        #利润模板构建
        revenue = sub_data.iloc[0]['营业收入']
        cost = sub_data.iloc[0]['营业成本']
        profit = sub_data.iloc[0]['净利润']
        prompt_list3 = []
        if isinstance(revenue, str):
            revenue = revenue.replace(",",'')
            if is_numeric(revenue):
                prompt_tmp = f'企业营业收入为{revenue}元；'
                prompt_list3.append(prompt_tmp)
        if isinstance(cost, str):
            cost = cost.replace(",",'')
            if is_numeric(cost):
                prompt_tmp = f'企业营业成本为{cost}元；'
                prompt_list3.append(prompt_tmp)

        if isinstance(profit, str):
            profit = profit.replace(",",'')
            if is_numeric(profit):
                prompt_tmp = f'企业净利润为{profit}元。\n'
                prompt_list3.append(prompt_tmp)
        if prompt_list3:
            prompt_tmp = '企业利润部分：' + ''.join(prompt_list3)
            prompt += prompt_tmp

    except Exception as e:
        print(e)

    return prompt



#
def _load_vector(company_name,year,embeddings):
    temp_year = int(year)
    temp_faiss = []
    try:
        company_year = f"{company_name}__{temp_year}年"
        temp_faiss = covert_data_vector_opening(company_year, embeddings)
        use_prompt = True
    except Exception as e:
        print(e)
    return temp_faiss


def load_prompt_vector(curret_faiss,question,cleaned_text,company,year,question_type):
    key_words = []
    prompt = ''
    # try:
    vector_store, temp_dict = curret_faiss
    if question_type == 'image':
        key_words = ['公司主要业务有哪些','公司主要经营模式是什么','社会责任','企业风险']
    if question_type == 'trend':
        key_words = ['发展战略','公司经营规划','产业趋势']
    if question_type == 'risk':
        key_words = ['企业面对风险']

    page_content_newlist_add = []
    for target,key_word in enumerate(key_words):
        #企业画像添加公司基本信息
        if question_type == 'image' and target == 0:
            base_situation = product_prompt_base(company, year)
            if base_situation:
                aspect_result = f"公司基本信息：\n{base_situation}"
                page_content_newlist_add.append(aspect_result)

        #实现检索
        if question_type != 'risk':
            top_content = vector_store.similarity_search(key_word, k=1)
        else:
            top_content = vector_store.similarity_search(key_word, k=3)
        # print(top_content)
        page_content_list = []
        for i, content in enumerate(top_content):
            value = content.page_content
            new_content = f"{value}"
            page_content_list.append(new_content)
        page_content_newlist = sorted(set(page_content_list), key=page_content_list.index)
        for index,j in enumerate(page_content_newlist):
            aspect_result = f"{key_word}：\n{j}"
            page_content_newlist_add.append(aspect_result)

        # 企业画像添加公司财务状况
        if question_type == 'image' and target == 1:
            money_situation = product_prompt_property(company, year)
            if money_situation:
                aspect_result = f"财务状况：\n{money_situation}"
                page_content_newlist_add.append(aspect_result)

    top_content_merge = "\n\n".join(page_content_newlist_add)
    if len(top_content_merge) > 3900:
        top_content_merge = top_content_merge[:3900]
    if question_type == 'image':
        prompt = f'{top_content_merge}\n=====\n上文是和问题【{question}】相关的企业画像内容，企业画像需要从公司基本信息、主要业务、经营模式、财务状况、社会责任和企业风险六个方面分别进行介绍。请根据上文回答用户的问题。\n{question}'
    elif question_type == 'trend':
        prompt = f'{top_content_merge}\n=====\n上文是和问题【{question}】相关的企业产业趋势内容。请根据上文回答用户的问题。\n{question}'
    elif question_type == 'risk':
        prompt = f'{top_content_merge}\n=====\n上文是和问题【{question}】相关的企业风险内容。请根据上文回答用户的问题。\n{question}'
    return prompt
    # except Exception as e:
    #     print(e)
    #     return question


def load_prompt_caiwu(question,company,year,question_type):
    key_words = []
    sub_data = df[(df['公司名称'] == company) & (df['年份'] == int(year))]
    # 公司基本信息构建
    prompt_excel = ''
    for index, i in enumerate(list_caiwu):
        if i not in sub_data.columns:
            continue
        value = sub_data.iloc[0][i]
        if value and isinstance(value, str) and value != '无':
            value = value.replace(",","")
            prompt_excel += f"{i}是{value}；"
    if prompt_excel:
        prompt = f'请仿照以下问题的回答风格，根据上下文内容生成答案。\n\n【回答风格】：\n问题：2019年中国工商银行总资产是多少元?\n答案：2019年中国工商银行总资产是12345678.9元。\n' \
                 f'问题：工商银行2019年营业外支出和营业外收入分别是多少元?\n答案：工商银行2019年营业外支出为12345678.9元，营业外收入为2345678.9元。\n====\n【上下文内容】：\n{company}年报数据：{prompt_excel}\n\n问题：{question}\n答案：'
    else:
        prompt = ''
    return prompt

if __name__ == '__main__':
    load_prompt_caiwu('',"中科创达软件股份有限公司",'2019','caiwu')