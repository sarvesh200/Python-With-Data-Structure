#!/usr/bin/env python
# coding: utf-8

# In[3]:


import heapq
MyHeap = [21,1,45,48,32,6]
heapq.heapify(MyHeap)
print(MyHeap)


#Replacing the element inside the heap

heapq.heapreplace(MyHeap,12)
print(MyHeap)


# In[ ]:




