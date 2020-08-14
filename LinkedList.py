#!/usr/bin/env python
# coding: utf-8

# In[3]:




class Node:  
    def __init__(self, dataval=None):  
        self.dataval = dataval  
        self.nextval = None  
class SLinkedList: 
    def __init__(self):  
        self.headval = None
    def listprint(self): 
        printval = self.headval  
        while printval is not None:  
            print (printval.dataval)
            printval = printval.nextval
    
    def AtBegining(self,newdata): 
        NewNode = Node(newdata)  # Update the new nodes next val to existing node 
        NewNode.nextval = self.headval  
        self.headval = NewNode
        
    def AtEnd(self, newdata):  
        NewNode = Node(newdata)  
        if self.headval is None:  
            self.headval = NewNode  
            return  
        laste = self.headval  
        while(laste.nextval):  
            laste = laste.nextval  
            laste.nextval=NewNode
    
    def Inbetween(self,middle_node,newdata):  
        if middle_node is None:  
            print("The mentioned node is absent")  
            return  
        
        NewNode = Node(newdata)  
        NewNode.nextval = middle_node.nextval  
        middle_node.nextval = NewNode

    def RemoveNode(self, Removekey):  
        HeadVal = self.head  
        if (HeadVal is not None):  
            if (HeadVal.data == Removekey):  
                self.head = HeadVal.next  
                HeadVal = None  
                return  
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            
            prev = HeadVal  
            HeadVal = HeadVal.next  
            
        if (HeadVal == None):
            return  
        prev.next = HeadVal.next 
        HeadVal = None








        
list1 = SLinkedList()  
list1.headval = Node("Mon") 
e2 = Node("Tue") 
e3 = Node("Wed")  
# Link first Node to second node  
list1.headval.nextval = e2
e2.nextval = e3
list.AtBegining("Sun")
list1.listprint()
list1.Inbetween(list1.headval.nextval,"Fri")
list1.AtEnd("SAT")
list1.RemoveNode("TUE")



# In[ ]:




