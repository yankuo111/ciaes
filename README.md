## 数据预处理
cd到data_preprocess目录下：
1.运行company_product.py文件
2.运行pdf2txt.py文件，将年报pdf转化为txt格式
3.运行cut_table_base.py、cut_table_fin.py、data_process.py文件将结构化数据转化为excel数据。
4.运行vector_product.py将非结构数据转化为Faiss向量库。



## 模型评估
cd到generateModel目录下：
运行python caculate_distance.py实现部分测试样例的结果准确率评估。

## 其它
1.bloomz环境安装包版本见requestment.txt文件
2.测试问题需要包含公司名称、年份和意图三个要素。公司名称见“问题中咨询的公司名称.json”文件。
例如：
交控科技股份有限公司2020年总资产是多少？
请构建2020年交控科技股份有限公司的画像。
分析2020年交控科技股份有限公司的产业趋势。
2020年交控科技股份有限公司的企业风险有哪些？

