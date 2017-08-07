import csv
import numpy as np
import math
import collections

def loadClass(filename):				#to load data from class labels file
	with open(filename, 'r') as f:
		data_list = []
		for x in f.readlines():
			tmp = x.split('\n')
			data = tmp[0].split(';')
			data_list.append(data)
		return data_list


def loadClass1(filename):				#to load data from class labels file
	with open(filename, 'r') as f:
		data_list = []
		for x in f.readlines():
			tmp = x.split('\n')
			data = tmp[0].split(',')
			data_list.append(data)
		return data_list


dataset = loadClass1('ratings_Health_and_Personal_Care.csv')		# user_id , product_id , rating , timestamp
dataset = np.array(dataset)				# load the data set
print dataset.shape


ratings = dataset[:,2]
ratings = np.array(ratings, dtype = np.float64)
print(np.unique(dataset[:,1]).shape)			# no of products

predicted_ratings = loadClass('mean_Health_and_Personal_Care.csv')				# product_id , rating 
		
predicted_ratings = np.array(predicted_ratings)				
print  predicted_ratings.shape
 
final_ratings = np.array(predicted_ratings[:,1] , dtype = np.float64)
average = np.mean(final_ratings)
final_ratings = final_ratings - average
print "average_predicted_rating" , average

c = collections.Counter(dataset[:,0])			# Reweighted modeling 2 : Remove non profilic authors
profilic_users = []
non_profilic_users = []
for i in c:
	if c[i] > 20:
		profilic_users.append(i)
	else :
		non_profilic_users.append(i)

print "no of products : " , len(np.unique(dataset[:,1]))
print "no of users : " , len(np.unique(dataset[:,0]))
print "no of profilic users : " , len(profilic_users)

helpfulness = []
for i in profilic_users:
	indices = np.array([i1 for i1, x in enumerate(dataset[:,0]) if x == i])
    	user_set = dataset[indices]
    
    	this_user_ratings = np.array(user_set[:,2], dtype = np.float64)
    	this_user_avg = np.mean(this_user_ratings)
    	this_user_ratings = this_user_ratings - this_user_avg
    
    	this_user_products = user_set[:,1]
    	indices = []
    	
    	for j,x in enumerate(predicted_ratings[:,0]) :
    		if x in  this_user_products.tolist() :
    			indices.append(j)
    	
    	predicted_ratings_usrproducts = final_ratings[indices]
    
    	a = np.sqrt( np.sum( np.square(predicted_ratings_usrproducts) ) ) 
    	b = a * np.sqrt( np.sum( np.square(this_user_ratings) ) ) 
    	
    	if b != 0 :
    		similarity = (np.dot(predicted_ratings_usrproducts , this_user_ratings)) / b
    	else :
    		similarity = -1
    	helpfulness.append([i , str(similarity)])
    

for i in non_profilic_users:
	helpfulness.append([i , str(-1)])
	

out = open('helfulness_Health_and_Personal_Care.csv', 'w')
for help_item in  helpfulness :
	out.write( str(help_item[0]) )
	out.write(';')
	out.write(help_item[1])
	out.write('\n')
	
out.close()


