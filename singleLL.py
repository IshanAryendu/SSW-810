class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listEle(self):
      res=[]
      printval = self.headval
      while printval is not None:
         res.append(printval.dataval)
         printval = printval.nextval
      return res

   # Print the linked list
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

   def AtBegining(self,newdata):
      NewNode = Node(newdata)
      # Update the new nodes next val to existing node
      NewNode.nextval = self.headval
      self.headval = NewNode
