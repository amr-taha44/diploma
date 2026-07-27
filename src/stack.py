class Stack:


  
  def __init__(self):
     self.items = []


  def is_empty(self):
    return len(self.items) == 0       

  def push_value(self, value):
    self.items.append(value)

  def pop_value(self):
    if self.is_empty ():
       raise IndexError("NO ITEMS IN STACK")   
    return self.items.pop()
  def get_peek(self):
    if self.is_empty():
          raise IndexError("NO ITEMS IN STACK")   
    return self.items[-1]
  def get_size(self):
    return len(self.items)
  #print("ammmmmmmmmmmmmmmm")