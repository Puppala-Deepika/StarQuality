import csv
import numpy as np
import math
import collections

def loadClass(filename):							#to load data from class labels file
	with open(filename, 'r') as f:
		data_list = []
		for x in f.readlines():
			tmp = x.split('\n')
			data = tmp[0].split(',')
			data_list.append(data)
		return data_list

dataset = loadClass('ratings_Health_and_Personal_Care.csv')
dataset = np.array(dataset)
print(dataset.shape)

print(np.unique(dataset[:,1]).shape)


										#Data for evaluation
from random import shuffle
from itertools import combinations
import random
n = 100
k = 10
uni , count = np.unique(dataset[:,0],return_counts=True)
yu = uni[count>=n]
test_data = []
test_set = []
test_labels = []
training_data = dataset
print len(training_data)
print len(yu)
j = 0 
for i in yu:
    indices = np.array([i1 for i1, x in enumerate(training_data[:,0]) if x == i])
    shuffle(indices)
    k_indices = combinations(indices[0:k],2)
    kl = []
    for n in k_indices:
    	kl.append(n)
    shuffle(kl)
    kl = kl[0:(k*k-3)]
    tl = []
    ts = []
    for n in kl:
    	if float(training_data[n[0]][2]) > float(training_data[n[1]][2]):
        	tl.append(training_data[n[0]][1])
        else:
        	tl.append(training_data[n[1]][1])
        ts.append([training_data[n[0]][1],training_data[n[1]][1]])
    test_labels.append(tl)
    test_set.append(ts)
    training_data = np.delete(training_data,indices[0:k],0)
print len(training_data) 
print len(test_set)

def loadClass2(filename):							#to load data from predicted ratings file
	with open(filename, 'r') as f:
		prod = []
		prod_mean = []
		for x in f.readlines():
			tmp = x.split('\n')
			data = tmp[0].split(';')
			prod.append(data[0])
			prod_mean.append(data[1])
		return prod,prod_mean

name = '_Health_and_Personal_Care.csv'						#set products, prod_means correspondingly
#products, prod_means = loadClass2('mean'+name)
#products, prod_means = loadClass2('median'+name)
#products, prod_means = loadClass2('lower_bound_normal'+name)
#products, prod_means = loadClass2('lower_bound_binomial'+name)
#products, prod_means = loadClass2('filter_out_non_prolific_authors_mean'+name)
#products, prod_means = loadClass2('filter_out_non_prolific_authors_median'+name)
#products, prod_means = loadClass2('filter_out_non_prolific_lower_bound_normal'+name)
products, prod_means = loadClass2('filter_out_non_prolific_lower_bound_binomial'+name)

predicted = []
for n in test_set:
    p = []
    for n1 in n:
        ks1 = products.index(n1[0])
        k1 = prod_means[ks1]
        ks2 = products.index(n1[1])
        k2 = prod_means[ks2]
        if float(k1) > float(k2):
        	p.append(n1[0])
        else:
        	p.append(n1[1])
    predicted.append(p)  
    
user = []									#to calculate accuracy
count = 0
count2 = 0
for i in range(0,len(test_set)):
    for j in range(0,len(test_set[i])):
    	count2 = count2+1
        if str(predicted[i][j]) == str(test_labels[i][j]):
            count = count+1

print "count  = ",count
print "count2 = ",count2
print "the accuaracy using the average method:",(1.0 * count / count2)      
