#!/usr/bin/env python
# coding: utf-8

# In[24]:


class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
        self.prev = None

        
class doublylinkedlist:
    
    def __init__(self):
        self.head =None
        
    #For Organising the data  
    def push(self,newval):
        NewNode = Node(newval)
        NewNode.next =self.head
        if self.head is not None:
            self.head.prev = NewNode
            self.head = NewNode
            
    def listprint(self):
        printval = self.head
        while(printval is not None):
            print(printval.data)
            printval =printval.next
            
            
dobj = doublylinkedlist()
dobj.push(20)
dobj.push(12)
dobj.push(10)
dobj.listprint()
        
    
            


# In[25]:


dobj.push(44)


# In[26]:


dobj.listprint()


# In[ ]:




