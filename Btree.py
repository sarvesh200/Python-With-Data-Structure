#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
        
#Insert method to create new node in our btree
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
                    
            elif data >self.data:
                
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
            
# a finding method to compare values with the different nodes
    def findingval(self, ival):
        if ival< self.data:
            if self.left is None:
                return str(ival)+ "Data Not Found"
            return self.left.findingval(ival)
        elif ival>self.data:
            if self.right is None:
                return str(ival)+ "Data Not Found"
            return self.right.findingval(ival)
        else:
            print(str(self.data)+"has been found")
            
# Function to print the tree

    def printtree(self):
        if self.left:
            self.left.printtree()
        
        print(self.data)
        
        if self.right:
            self.right.printtree()
            
root = Node(25)
root.insert(8)
root.insert(26)
root.insert(5)

print(root.findingval(14))
print(root.findingval(5))


            


# In[ ]:




