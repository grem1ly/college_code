import glob
import pickle

my_pred = open('../output/predictions.txt', 'r')
my_pred_text = my_pred.readlines()

my_key = []
for entry in my_pred_text:
    if 'pos' in entry:
        my_key.append('pos')
    if 'neg' in entry:
        my_key.append('neg')
print(my_key)
        
        

actual = open('../data/devkey.txt', 'r')
actual_text = actual.readlines()

act_key = []
for entry in actual_text:
    if 'pos' in entry:
        act_key.append('pos')
    if 'neg' in entry:
        act_key.append('neg')
print(act_key)


import numpy as np
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(act_key, my_key)
print(accuracy)


key = open("../data/devkey.txt", 'r')
pred = open("../output/predictions.txt", 'r')

keyContent = key.read()
predContent = pred.read()

keyArr = keyContent.split('\n')
predArr = predContent.split('\n')

correctPos = 0
correctNeg = 0

numPos = 0
numNeg = 0

classifiedAsPos = 0
classifiedAsNeg = 0

for i in range(len(keyArr)):
	keyStr = keyArr[i]
	predStr = predArr[i]
	if "pos" in keyStr and "pos" in predStr:
		correctPos += 1
	if "neg" in keyStr and "neg" in predStr:
		correctNeg += 1
		
for keyStr in keyArr:
	if "pos" in keyStr:
		numPos += 1
	if "neg" in keyStr:
		numNeg += 1
		
for predStr in predArr:
	if "pos" in predStr:
		classifiedAsPos += 1
	if "neg" in predStr:
		classifiedAsNeg += 1

precisionNeg = correctNeg/classifiedAsNeg
recallNeg = correctNeg/numNeg
negF1 = 2*precisionNeg*recallNeg/(precisionNeg+recallNeg)

precisionPos = correctPos/classifiedAsPos
recallPos = correctPos/numPos
posF1 = 2*precisionPos*recallPos/(precisionPos+recallPos)

print("Neg (precision, recall, f1):", precisionNeg, recallNeg, negF1)
print("Pos (precision, recall, f1):", precisionPos, recallPos, posF1)
