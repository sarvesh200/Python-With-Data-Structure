#!/usr/bin/env python
# coding: utf-8

# In[17]:


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data =data
    
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data =data
        
    
        
    def printTree(self):
        if self.left:
            self.left.printTree()
            
        print(self.data)
        if self.right:
            self.right.printTree()
        
        
        
       
        
        
          
        
        
        
        
      
        

root =Node(24) 
root.printTree()
root.insert(25)
root.insert(29)
root.insert(18)
root.insert(20)


# In[18]:


root.printTree()


# In[ ]:




