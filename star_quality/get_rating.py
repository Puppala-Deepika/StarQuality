import csv
import numpy as np
import math
import collections

def loadClass(filename):				#to load data from class labels file
	with open(filename, 'r') as f:
		data_list = []
		for x in f.readlines():
			tmp = x.split('\n')
			data = tmp[0].split(',')
			data_list.append(data)
		return data_list

dataset = loadClass('ratings_Electronics.csv')
dataset = np.array(dataset)
print(dataset.shape)

name = '_Electronics.csv'
ratings = dataset[:,2]
ratings = np.array(ratings, dtype = np.float32)
print(np.unique(dataset[:,1]).shape)

out = open('mean'+name, 'w')
for each_product in np.unique(dataset[:,1]):		#to predict rating from mean
	product_set = ratings[dataset[:,1] == each_product]
	out.write(each_product)
	out.write(';')
	out.write(str(np.mean(product_set)))
	out.write('\n')
out.close()	
print("Completed predicting rating from mean")


out = open('median'+name, 'w')			#to predict rating from median
for each_product in np.unique(dataset[:,1]):
	product_set = ratings[dataset[:,1] == each_product]
	out.write(each_product)
	out.write(';')
	out.write(str(np.median(product_set)))
	out.write('\n')
out.close()
print("Completed predicting rating from median")


out = open('lower_bound_normal'+name, 'w')		#to predict rating from lower bound Normal metric
for each_product in np.unique(dataset[:,1]):
	product_set = ratings[dataset[:,1] == each_product]
	out.write(each_product)
	out.write(';')
	out.write(str(np.mean(product_set) - (1.96*np.var(product_set))/(math.sqrt(product_set.shape[0]))))
	out.write('\n')
out.close()
print("Completed predicting rating from lower bound normal metric")


out = open('lower_bound_binomial'+name, 'w')		#to predict rating from lower bound binomial
for each_product in np.unique(dataset[:,1]):
	product_set = ratings[dataset[:,1] == each_product]
	n = product_set.shape[0]
	t = np.array(np.where(product_set >= 4)).shape
	proportion = t[0]/n
	proportion_n = 1-proportion
	z = 1.96
	out.write(each_product)
	out.write(';')
	l = proportion+((1.96*0.98)/n)
	r = ((proportion*proportion_n)+(0.98*0.98/n))/n
	r = math.sqrt(r)
	d = r/ (1+(1.96*1.96/n))
	out.write(str(l-1.96*r))
	out.write('\n')
out.close()
print("Completed predicting rating from lower bound binomial metric")


c = collections.Counter(dataset[:,0])
l = []
for i in c:
	if c[i] > 9:
		l.append(dataset[dataset[:,0]==i])
modified_dataset = l[0]
for i in range(1, len(l)):
	modified_dataset = np.append(modified_dataset, l[i])
n = int(modified_dataset.shape[0]/4)
modified_dataset = modified_dataset.reshape((n,4))
print(modified_dataset.shape)
ratings = modified_dataset[:,2]
ratings = np.array(ratings, dtype = np.float32)

out = open('filter_out_non_prolific_authors_mean'+name, 'w')		#predicting rating from mean metric after filtering out non prolific authors
for each_product in np.unique(modified_dataset[:,1]):
	product_set = ratings[modified_dataset[:,1] == each_product]
	out.write(each_product)
	out.write(';')
	out.write(str(np.mean(ratings[modified_dataset[:,1] == each_product])))
	out.write('\n')
out.close()
print("Completed predicting rating from mean metric after filtering out non prolific authors")


out = open('filter_out_non_prolific_authors_median'+name, 'w')		#predicting rating from median metric after filtering out non prolific authors
for each_product in np.unique(modified_dataset[:,1]):
	product_set = ratings[modified_dataset[:,1] == each_product]
	out.write(each_product)
	out.write(';')
	out.write(str(np.median(ratings[modified_dataset[:,1] == each_product])))
	out.write('\n')
out.close()
print("Completed predicting rating from median metric after filtering out non prolific authors")

out = open('filter_out_non_prolific_lower_bound_normal'+name, 'w')		#predicting rating from lower bound normal metric after filtering out non prolific authors
for each_product in np.unique(modified_dataset[:,1]):
	product_set = ratings[modified_dataset[:,1] == each_product]
	out.write(each_product)
	out.write(';')
	out.write(str(np.mean(product_set) - (1.96*np.var(product_set))/(math.sqrt(product_set.shape[0]))))
	out.write('\n')
out.close()
print("Completed predicting rating from lower bound normal metric after filtering out non prolific authors")


out = open('filter_out_non_prolific_lower_bound_binomial'+name, 'w')		#predicting rating from lower bound binomial metric after filtering out non prolific authors
for each_product in np.unique(modified_dataset[:,1]):
	product_set = ratings[modified_dataset[:,1] == each_product]
	n = product_set.shape[0]
	t = np.array(np.where(product_set >= 4)).shape
	proportion = t[0]/n
	proportion_n = 1-proportion
	z = 1.96
	out.write(each_product)
	out.write(';')
	l = proportion+((1.96*0.98)/n)
	r = ((proportion*proportion_n)+(0.98*0.98/n))/n
	r = math.sqrt(r)
	d = r/ (1+(1.96*1.96/n))
	out.write(str(l-1.96*r))
	out.write('\n')
out.close()
print("Completed predicting rating from lower bound binomial metric after filtering out non prolific authors")

