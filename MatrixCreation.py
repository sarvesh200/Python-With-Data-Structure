#!/usr/bin/env python
# coding: utf-8

# In[7]:


from numpy import *
MyMatrix = array([['John',92,78,85,88],['Jenny',85,71,72,90],['Bob',88,95,97,99],['sam',88,95,97,99],['Jane',88,95,97,99],['Marry',88,95,97,92]])
ReshapedMatrix = reshape(MyMatrix,(6,5))

#Updating the matrix including row
ReshapedMatrix[4] = ['Alan',11,11,11,11]

print(ReshapedMatrix)




# In[ ]:




