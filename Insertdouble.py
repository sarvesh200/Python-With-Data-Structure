#!/usr/bin/env python
# coding: utf-8

# In[24]:


class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
        self.prev = None

class doublylist:
    
    def __init__(self):
        self.head = None
        
        
    def push(self,newval):
        NewNode =Node(newval)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
    
    def append(self,newval):
        NewNode = Node(newval)
        NewNode.next = None
        
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        
        last = self.head
        while(last.next is not None):
            last = last.next
            
        last.next = NewNode   #lastnode  newnode
        NewNode.prev = last
        return
        
    
            
    
    def listprint(self):
        printval =self.head
        
        while printval is not None:
            print(printval.data)
            printval =printval.next
            
            
dobj = doublylist()
dobj.push(22)
dobj.push(20)
dobj.push(15)
dobj.listprint()
        


# In[27]:


dobj.append(24)


# In[28]:


dobj.listprint()


# In[ ]:




