#!/usr/bin/env python
# coding: utf-8

# In[46]:


class Node:
    def __init__(self,dataval = None):
        self.dataval =dataval
        self.nextval = None
        
class LinkedList:
    def __init__(self):
        self.headval = None
        
        #Inserting node at the start of linked list
        def AtBegining(self,newdata):  
            NewNode = Node(newdata) 
            NewNode.nextval = self.headval
            self.headval = NewNode


   
        
     # Function to traverse the likedlist 
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    
    
    
list = LinkedList()
list.headval = Node("Jan")
m2 = Node("Feb")
m3 = Node("Mar")

#Linking of the nodes
list.headval.nextval = m2

m2.nextval = m3


# In[47]:


list.listprint()


# In[48]:


list.RemoveNode("Mar")


# In[49]:


list.listprint()


# In[ ]:




