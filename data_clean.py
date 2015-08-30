# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import csv
import numpy as np
import pandas as pd


df = pd.read_excel('test_data.xlsx')
# df.to_csv('test_data.csv', index = False, encoding = 'utf-8')


df = pd.read_csv('test_data.csv')
# print df.columns
df['content'] = df[u'发布内容'].apply( lambda s: s.partition("//")[0])
df['content'] = df['content'].apply( lambda s: s.partition("【")[0])
df['content'] = df['content'].apply( lambda s: s.partition("#女司机惨遭男司机暴打# 男的过火了。女的也欠揍。请在13点发布。")[0])

df.to_excel('test_data.xlsx', index = False)
