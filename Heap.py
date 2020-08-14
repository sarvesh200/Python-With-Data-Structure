#!/usr/bin/env python
# coding: utf-8

# In[1]:


import heapq

MyHeap = [12,45,98,34,55]

# Using heapify function to rearrange the elements
heapq.heapify(MyHeap)
print(MyHeap)


# In[8]:


import heapq

NewHeap = [1,3,5,78,21,45]
heapq.heapify(NewHeap)
print(NewHeap)

#Remove element from the heap
heapq.heappop(NewHeap)
print(NewHeap)


# In[ ]:




