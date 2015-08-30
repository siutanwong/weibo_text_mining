#!/usr/bin/env python
#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import csv
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB
from mmseg import seg_txt
import jieba

########### step1: Import training data from the excel spreadsheet into pandas dataframe.
df = pd.read_excel("train_after5.xlsx")
print df[u'content']
# print df.columns
# df['发布内容']

# Try to tokenize the weibo contents, but we found out that cut_for_search is a better function.
# for i in df['发布内容']:
# 	result = jieba.tokenize(i,mode='search')
# for tk in result:
#     print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))


########### step2: Prepare for text analysis, use the "jieba" package to segment the Chinese sentences on weibo.
def add_spaces(string):
	seg_list = jieba.cut_for_search(string) 
	try:
		# Successfully return
		return " ".join(seg_list)
	except:
		# Gets that error
		return ""

# Use .apply to create a new column with the tokenized Chinese words.
train_content = df[u'content'].apply(add_spaces)

train_attitude = df[u'态度']# convert column name to English
# print df['attitude']

# Clean the mannully input attitude into numbers that computer can analysis
encoder = preprocessing.LabelEncoder()
correct_attitude = encoder.fit_transform(train_attitude)
# print correct_attitude


# Try to munnally add a stop-word list, but it is already built in the cut_for_search function.
# sw = [ w.strip() for w in open( "stop_words.txt","rU" ).readlines() ]


########### step3: Extracting features...
# vectorizer=TfidfVectorizer()  
vectorizer = HashingVectorizer(non_negative=True)
train_data = vectorizer.fit_transform(train_content)
# train_data = vectorizer.fit_transform(train_content).toarray()
# for item in vectorizer.get_feature_names():
#     print item


########### step4: build a model for our training data
# model = DecisionTreeClassifier()
# fit_model = model.fit(train_data, correct_attitude)
model = MultinomialNB(alpha = 0.01)
fit_model = model.fit(train_data, correct_attitude)


########### step5: Evaluate our model with 10-fold cross-validation
scores = cross_validation.cross_val_score(model, train_data, correct_attitude, cv=5)
print "Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)


########## step6: Applying the model
df2 = pd.read_excel("test_after5.xlsx")
test_data = df2[u'content'].apply(add_spaces)
test_content = vectorizer.transform(test_data)
df2['attitude'] = [encoder.classes_[model.predict(test_content.toarray()[i])] for i in xrange(len(test_data))]

for i in xrange(len(test_data)):
        print '%s -> %s' % (test_data[i], encoder.classes_[model.predict(test_content.toarray()[i])])

