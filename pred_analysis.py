# encoding=utf-8

import sys
sys.path.append('../')
import jieba
import jieba.analyse
from optparse import OptionParser

# Import data from txt file, split data into content and attitude.
test = [line.strip().split('->') for line in open('pred_before5.txt').readlines()]
content = [i[0] for i in test if len(i) > 1]
attitude = [i[1] for i in test if len(i) > 1]

# Turn the attitude list into a list of string.
attitude_num = []
for item in attitude:
	if len(item) == 5:
		attitude_num.append(item[2:4])
	else:
		attitude_num.append(item[2])
# print attitude_num

negative_att = len([i for i in attitude_num if i == "-1"])
possitive_att = len([i for i in attitude_num if i == "1"])

# Get the % of comments that thought the women deserved to be beaten)
print float(possitive_att)/len(test)


# Use TFIDF to extract the key words from over 7000 tweets.
keywords = jieba.analyse.extract_tags(" ".join(content), topK=20, withWeight=False, allowPOS=())
for i in keywords:
	print i


