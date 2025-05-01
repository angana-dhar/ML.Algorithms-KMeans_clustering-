#!/usr/bin/env python
# coding: utf-8

# # using SKlearn
# 

# In[2]:


#create fake income/age clusters for N people in k clusters 
def createClusterddata(N,k):
    random.seed(10)
    pointsPerCluster = float(N)/k
    x = []
    for i in range (k):
        incomeCentroid = random.uniform(20000.0 , 200000.0)
        ageCentroid = random.uniform(20.0,70.0)
        for j in range(int(pointsPerCluster)):
            x.append([np.random.normal(incomeCentroid,10000.0),np.random.normal(ageCentroid,2.0)])
    x = np.array(x)
    return x

#If N=100 and k=4, you'll get 4 distinct clusters of 25 (income, age) points each.



# In[7]:


import random 
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

data = createClusterddata(100,5)
scaled_data = scale(data)


#Scaling the data hepls to normalize the data for good results 
#creating and fit KMEANS model 
model = KMeans(n_clusters = 5)
model = model.fit(scale(data))
# Print labels
print("Cluster labels:", model.labels_)


# In[8]:


plt.scatter(scaled_data[:,0],scaled_data[:,1], c=model.labels_)
plt.title("KMeans Clustering of Income vs Age")
plt.xlabel("Income(scaled)")
plt.ylabel("Age(scaled)")
plt.show()


# In[ ]:




