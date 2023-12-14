##!/usr/bin/python3

# @File: uploadFileWork.py

# -*-coding:utf-8-*-

# @Author:Guan_pc

# @Time: 2023年04月12日15时

# 说明:
import os
import re
import time
import zipfile
from collections import Counter
from io import BytesIO

from bson import ObjectId
from lxml import html

from app.config import cacheUpload, resStand, supportFile, cacheDownload
from app.createApp import app
from database.tables import KnowledgeList
from generateModel.knowledgeSearch.langChainSearch import knowledgeManager

etree = html.etree
from pydocx.export import PyDocXHTMLExporter
# from generateModel.knowledgeSearch.featureModel import robertaVec
# from generateModel.knowledgeSearch.keyWord import keyWord

from database.mongodb import insertFile, mongoNodeVec, mydb, getFile


class MyPyDocXHTMLExporter(PyDocXHTMLExporter):

    def __init__(self, path):
        super(MyPyDocXHTMLExporter, self).__init__(path=path)

    # 不显示被删除的内容
    def export_deleted_run(self, deleted_run):
        return


def rdoc2docx(filePath):
    cache_dir = os.path.split(filePath)[0]
    if not os.path.isdir(cache_dir):
        os.mkdir(cache_dir)
    doc_file = filePath
    docx_file = os.path.join(cache_dir, list(os.path.split(filePath))[-1][:-3] + 'docx')
    try:
        flag = os.system(f'soffice --convert-to docx "{doc_file}" --outdir "{cache_dir}"')
        if flag:
            os.system(f'libreoffice6.4 --headless --convert-to docx {doc_file} --outdir {cache_dir}')
        os.remove(doc_file)
        return docx_file
    except Exception as e:
        print(e)
        return ''


def getPiecesFromHtml(paghs):
    out = []
    for index, p in enumerate(paghs):
        if len(p.xpath('.//*[@class="pydocx-hidden"]')) > 0:
            continue
        text = str(p.xpath('string()'))
        text = re.sub(r'^ {1,}', '', text)
        text = re.sub(r' {1,}$', '', text)
        if not text:
            continue
        tag = p.tag
        attrib = str(p.attrib)
        if tag == 'ol':
            lis = p.getchildren()
            for li in lis:
                textsub = []
                for span in li.getchildren():
                    text = '\n'.join(span.xpath('.//text()'))
                    text = re.sub(r'^ {1,}', '', text)
                    text = re.sub(r' {1,}$', '', text)
                    if not text:
                        continue
                    ifTitle = 'pydocx-center' in str(span.attrib) or len(span.xpath('.//*[@class="pydocx-center"]')) > 0
                    if ifTitle:
                        if textsub:
                            out.append((0, '\n'.join(textsub), 1))
                            textsub = []
                        out.append((int(ifTitle), text, 1))
                    else:
                        textsub.append(text)
                if textsub:
                    out.append((0, '\n'.join(textsub), 1))
        elif tag == 'p' or tag == 'h1' or tag == 'h2':
            ifTitle = 'pydocx-center' in attrib or len(p.xpath('.//*[@class="pydocx-center"]')) > 0
            out.append((int(ifTitle), text, 0))
        elif tag == 'table':
            text = pretable(p)
            out.append((0, text, 0))
        else:
            pass
    return out


def pretable(p):
    out = []
    trs = p.getchildren()
    for tr in trs:
        tds = tr.getchildren()
        row = []
        for td in tds:
            text = td.xpath('string()')
            row.append(text)
        out.append(' '.join(row))
    table = '\n'.join(out)
    return table


def isfirst(text):
    res = re.match(r'^[\d\.]+', text)
    if res:
        titleList = [i for i in res.group().split('.') if i]
        if len(titleList) == 1:
            if text[res.end() - 1] != '．':
                return True
    elif re.match(r'^第[\u4e00-\u9fa5\u767e\u5343\u96f6]{1,10}章', text):
        return True
    elif re.match(r'^附件：', text):
        return True
    elif re.match(r'^[\u4e00-\u9fa5\u767e\u5343\u96f6]{1,10}、', text):
        return True
    else:
        return False


def issecend(text):
    titleRe = re.match(r'^[\d\.]+', text)
    if titleRe:
        titleList = [i for i in titleRe.group().split('.') if i]
        if len(titleList) == 2:
            return True
    if re.match(r'^第[\u4e00-\u9fa5\u767e\u5343\u96f6]{1,10}条', text):
        return True
    return False


def getdeep(text):
    titleRe = re.match(r'^[\d\.]+', text)
    if titleRe:
        titleList = [i for i in titleRe.group().split('.') if i]
        return len(titleList) - 1
    else:
        return False


def standSent(part):
    if part[0]:
        if part[1][0] == '图' or part[1][0] == '表':
            return -1, part[1]
        else:
            return 0, part[1]  # -1表示正文，需并入上个标题下; 0表示以及标题；1表示二级标题；2表示三级......
    else:
        if part[2]:
            return 1, part[1]
        else:
            if isfirst(part[1]):
                return 0, part[1]
            elif issecend(part[1]):
                return 1, part[1]
            elif getdeep(part[1]):
                deep = getdeep(part[1])
                return deep, part[1]
            else:
                return -1, part[1]


def smartJoin(pieces):
    out = pieces[0]
    for piece in pieces[1:]:
        if re.search(r'[^\u4e00-\u9fa5]', out[-1] + piece[0]):  # 如果两段文本之间是汉字与汉字相连，则不换行。
            out += '\n' + piece
        else:
            out += piece
    return out


# def buildContentTree(root):
#     peices = [(index, i) for index, i in enumerate(root['data']) if i[0] == root['deep']]
#     peices.append((len(root['data']), ''))
#     inindex = root['index']
#     children = []
#     for index, (dataIndex, p) in enumerate(peices[:-1]):
#         dataBegin = dataIndex + 1
#         dataEnd = peices[index + 1][0]
#         node_index = f'{inindex}-{index}'
#         sentenceVec = robertaVec(p[1])
#         keyWord_ = keyWord(p[1])
#         if dataEnd == dataBegin and (len(p[1]) > 20 or '附件' in p[1]):  # 规定叶子结点且长度大于20的节点的内容有实际意义。
#             contentFlag = 1
#         else:
#             contentFlag = 0
#         id = mongoNodeVec.insert_one({'index': node_index, 'sentenceVec': sentenceVec})
#         child = {'deep': root['deep'] + 1, 'index': node_index, 'desc': p[1],
#                  'data': root['data'][dataBegin:dataEnd], 'sentenceVec': str(id.inserted_id), 'isContent': contentFlag,
#                  'keyWord': keyWord_, 'textLen': len(p[1])}
#         child = buildContentTree(child)
#         children.append(child)
#     root['children'] = children
#     root.pop('data')
#     return root


def findName(filename):
    titleStr = filename
    titles = re.findall(r'《(.+?)》', titleStr)
    if titles:
        max_count = 0
        title = ''
        titles = Counter(titles)
        for title_, count in titles.items():
            if count > max_count:
                max_count = count
                title = title_
    else:
        title = "".join(re.split(f'(\.)', filename)[:-2])
    return title


def uploadwork(filePath, knowledgeId):
    dbName = f'knowledge{knowledgeId}'
    sourceFileName = os.path.split(filePath)[1]
    isInsert = mydb[dbName].find_one({'sourceFile.fileName': sourceFileName})
    if isInsert:
        print(f'{sourceFileName}已入库')
        return '已入库'
    source_html = MyPyDocXHTMLExporter(filePath).export()
    policyName = findName(sourceFileName)

    createTime = int(time.time())
    sourceFile = {
        'id': insertFile(filePath),
        'fileName': os.path.split(filePath)[1]
    }
    data = {
        'createTime': createTime,
        'policyName': policyName,
        'sourceFile': sourceFile,
        'source_html': source_html
    }
    id = mydb[dbName].insert_one(data).inserted_id
    app.logger.info(f'{sourceFileName} 入库成功')
    knowledgeCache = knowledgeManager.get(knowledgeId)
    knowledgeCache.insertDoc(filePath, fileId=id)


def delPolocy(userId, knowledgeId, policy_id):
    policy_id = eval(policy_id)
    count = KnowledgeList.query.filter(KnowledgeList.createUserId == userId,
                                       KnowledgeList.uniqueId == knowledgeId).count()
    if count == 0:
        return resStand(6002, '', '没有权限操作当前知识库').tojson()
    dbName = f'knowledge{knowledgeId}'
    knowledgeCache = knowledgeManager.get(knowledgeId)
    oks = 0
    for _id in policy_id:
        count = mydb[dbName].find_one({'_id': ObjectId(_id)})
        if count:
            knowledgeCache.delDoc(_id)
            oks += 1
            mydb[dbName].delete_one({'_id': ObjectId(_id)})
    knowledgeCache.saveChange()
    result = {
        'delFileNum': oks,
        'fieldNum': len(policy_id) - oks
    }
    for key in list(knowledgeManager.keys()):
        if '[' in key and str(knowledgeId) in key:
            knowledgeManager.delete(key)
    return resStand(0, result, 'success').tojson()


def savefile(upfiles, userId, knowledgeId):
    count = KnowledgeList.query.filter(KnowledgeList.createUserId == userId,
                                       KnowledgeList.uniqueId == knowledgeId).count()
    if count == 0:
        return resStand(6002, '', '没有权限操作当前知识库').tojson()
    if not os.path.exists(cacheUpload):
        os.makedirs(cacheUpload)
    filepaths = []
    for file in upfiles:
        filePath = os.path.join(cacheUpload, file.filename)
        if filePath.endswith(supportFile):
            if filePath.endswith('wps'):
                filePath = filePath[:-3] + 'doc'
            file.save(filePath)
            filepaths.append(filePath)
        else:
            pass
    result = fun4fileUpload(filepaths, knowledgeId)
    return result


# @async_fun
def fun4fileUpload(filepaths, KnowledgeId):
    oks = []
    field = []
    for filepath in filepaths:
        fileName = os.path.split(filepath)[-1]
        if fileName.lower().endswith('.doc'):
            filepath = rdoc2docx(filepath)
            fileName = os.path.split(filepath)[-1]
        try:
            uploadwork(filepath, KnowledgeId)
            oks.append(fileName)
            os.remove(filepath)
        except:
            os.remove(filepath)
            field.append(fileName)
    result = {
        'uploaded': oks,
        'field': field
    }
    knowledgeManager.get(KnowledgeId).saveChange()
    for key in list(knowledgeManager.keys()):
        if '[' in key and str(KnowledgeId) in key:
            knowledgeManager.delete(key)
    return resStand(0, result, 'success').tojson()


def downloadWork(userId, knowledgeId, ids):
    knowLedge = KnowledgeList.query.filter(KnowledgeList.createUserId == userId,
                                           KnowledgeList.uniqueId == knowledgeId).first()
    if knowLedge == None:
        return resStand(6002, '', '没有权限操作当前知识库').tojson()
    if not os.path.exists(cacheDownload):
        os.makedirs(cacheDownload)
    ids = eval(ids)
    if len(ids) > 1:
        in_memory_zip = BytesIO()
        with zipfile.ZipFile(in_memory_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
            for file in ids:
                fileName = file['fileName']
                fileId = file['id']
                fileByte = getFile(fileId)
                filePath = os.path.join(cacheDownload, fileName)
                with open(filePath, 'wb') as f:
                    f.write(fileByte)
                zf.write(filePath, arcname=fileName)
                os.remove(filePath)
        in_memory_zip.seek(0)
        return in_memory_zip, f'{knowLedge.knowledgeName}.zip'
    elif len(ids) == 1:
        file = ids[0]
        fileName = file['fileName']
        fileId = file['id']
        fileByte = getFile(fileId)
        return fileByte, fileName
    else:
        return resStand(6003, '', '未指定下载内容').tojson()


# 解决有几条法规的方法
if __name__ == '__main__':
    #####构建knowledge1 行内制度知识库
    # root = r'F:\python\Git\hxbregulation\data\信息科技制度'
    # time.sleep(5)
    # for index, i in enumerate(os.listdir(root)):
    #     if index < 0:
    #         continue
    #     path = os.path.join(root, i)
    #     # path = r'G:\python\Git\HxbRegulation_\data\信息科技制度\11.收文传阅华银制〔2017〕122号关于印发《华夏银行总行信息科技应用开发类需求实施工作量估算实施细则》的通知'
    #     addFiles = [os.path.join(path, file) for file in os.listdir(path) if '关于' not in file]
    #     file = [os.path.join(path, file) for file in os.listdir(path) if '关于' in file and file.endswith('docx')][0]
    #     print(index)
    #     uploadwork(file, 1)

    ####  构建knowledge2 龙公司制度知识库
    # root = r'F:\python\Git_new\llm-chat\data\公司制度'
    # policy_keyword = ['意见', '细则', '规程', '规定', '指引', '制度', '办法', '规范', '指南', '手册', '的函', '预案', '通知', '计划', '规划']
    #
    #
    # def get_allfile(path, file_list):
    #     dir_list = os.listdir(path)
    #     for x in dir_list:
    #         new_x = os.path.join(path, x)
    #         if os.path.isdir(new_x):
    #             get_allfile(new_x, file_list)
    #         elif os.path.isfile(new_x):
    #             file_list.append(new_x)
    #     return file_list
    #
    #
    # a = []
    # allFile = get_allfile(root, a)
    # file_need = []
    # for file in allFile:
    #     fileName = os.path.split(file)[-1]
    #     if fileName.lower().endswith('docx'):
    #         if '龙科制' in fileName:
    #             file_need.append(file)
    #         elif any([i in fileName for i in policy_keyword]):
    #             file_need.append(file)
    # for index, filePath in enumerate(file_need):
    #     print(index)
    #     print(filePath)
    #     uploadwork(filePath, 2)

    #### 构建中国法律法规知识库

    # import pymongo, gridfs
    # from tqdm import tqdm
    # from bson import ObjectId
    # myclient = pymongo.MongoClient('mongodb://admin:admin@106.38.203.210:17359/')
    # mydb_ = myclient['web-spider']
    # mongoFile = gridfs.GridFS(mydb_, 'lawFile')
    # chinaLawDB = mydb_['chinaLaw']
    # data_row = chinaLawDB.find()
    # totlecount = chinaLawDB.count_documents({})
    # saveDir = r'E:\中国法律数据'
    # # time.sleep(60)
    # for data in tqdm(data_row, total=totlecount):
    #     if '有效' in data['Timeliness']:
    #         fileobj = data['originFile']
    #         saveFile = os.path.join(saveDir, fileobj.get('fileName'))
    #         if not os.path.isfile(saveFile):
    #             with open(saveFile, 'wb') as f:
    #                 file = mongoFile.get(ObjectId(fileobj.get('fileId'))).read()
    #                 f.write(file)
    #         if saveFile.endswith(('doc','docx')):
    #             try:
    #                 uploadwork(saveFile, 7)
    #             except Exception as e:
    #                 print(e)
    #                 print('upfiled:',saveFile)

    ####  构建knowledge8 投顾知识库
    root = r'F:\python\Git_new\llm-chat\data\A1.4蓝鲸'


    def get_allfile(path, file_list):
        dir_list = os.listdir(path)
        for x in dir_list:
            new_x = os.path.join(path, x)
            if os.path.isdir(new_x):
                get_allfile(new_x, file_list)
            elif os.path.isfile(new_x):
                file_list.append(new_x)
        return file_list


    a = []
    allFile = get_allfile(root, a)
    file_need = []
    for file in allFile:
        fileName = os.path.split(file)[-1]
        if fileName.lower().endswith(('docx', 'doc')):
            file_need.append(file)
    for index, filePath in enumerate(file_need):
        print(index)
        print(filePath)
        uploadwork(filePath, 8)

    ####  构建knowledge9 智能投研
    root = r'F:\python\Git_new\llm-chat\data\基金信息'


    def get_allfile(path, file_list):
        dir_list = os.listdir(path)
        for x in dir_list:
            new_x = os.path.join(path, x)
            if os.path.isdir(new_x):
                get_allfile(new_x, file_list)
            elif os.path.isfile(new_x):
                file_list.append(new_x)
        return file_list


    a = []
    allFile = get_allfile(root, a)
    file_need = []
    for file in allFile:
        fileName = os.path.split(file)[-1]
        if fileName.lower().endswith(('docx', 'doc')):
            file_need.append(file)
    for index, filePath in enumerate(file_need):
        print(index)
        print(filePath)
        uploadwork(filePath, 9)
