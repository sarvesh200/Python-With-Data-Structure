#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Queue:  
    def __init__(self):  
        self.queue = list()  
    def addtoq(self,dataval):  # Insert method to add element  
        if dataval not in self.queue:  
            self.queue.insert(0,dataval)  
            return True  
        return False  
    def size(self):  
        return len(self.queue)  
    
    def removefromq(self):
        if len(self.queue)>0:  
            return self.queue.pop()  
        return ("No elements are in the Queue!")




TheQueue = Queue()  
TheQueue.addtoq("Mon")  
TheQueue.addtoq("Tue")  
TheQueue.addtoq("Wed")  
print(TheQueue.size())


