#!/bin/python3
class List:
  def __init__(self, value=None):
    self.val = value
    self.next = None

class DList(List):
  def __init__(self, value=None):
    List.__init__(self)
    self.prev = None
    self.val = value

class ListHead: 
  def __init__(self):
    self.head = None

  def add(self, val):
    l = List(val)
    tracer = self.head
    if (tracer == None):
      self.head = l
      return
    while (tracer.next != None):
      tracer = tracer.next
    tracer.next = l

  def insert(self, val):
    l = List(val) 
    l.next = self.head
    self.head = l

  def remove(self, val): 
    tracer = self.head
    index = 0
    if (self.head.val == val):
      self.head = self.head.next
      return index
    index += 1
    while (tracer.next != None and tracer.next.val != val):
      tracer = tracer.next
      index += 1
    if (tracer.next == None):
      print(f"Failed to find value {val} in list")
      return -1
    tracer.next = tracer.next.next # remove the value
    return index

  def print(self):
    print("Printing linked list (forward)")
    tracer = self.head
    index = 0
    if (tracer == None):
      print("Empty list.")
      return -1
    while (tracer != None):
      print(f"Index: {index}\t - {tracer.val}")
      tracer = tracer.next
      index += 1


class CListHead(ListHead):
  def __init__(self):
    ListHead.__init__(self)
    self.tail = None
  
  def add(self, val):
    l = DList(val)
    tracer = self.head
    if (tracer == None):
      self.head = l
      self.tail = l
      return
    while (tracer.next != None):
      tracer = tracer.next
    l.prev = tracer
    tracer.next = l
    self.tail = l

  def insert(self, val):
    l = DList(val) 
    l.next = self.head
    self.head.prev = l # Circular
    self.head = l  
    if (self.tail == None):
      self.tail = self.head

  def remove(self, val): 
    tracer = self.head
    index = 0
    if (self.head.val == val):
      self.head = self.head.next
      return index
    index += 1
    while (tracer.next != None and tracer.next.val != val):
      tracer = tracer.next
      index += 1
    if (tracer.next == None):
      print(f"Failed to find value {val} in list")
      return -1
    tracer.next = tracer.next.next # remove the value
    if (tracer.next == None):
      self.tail = tracer
    else: 
      tracer.next.prev = tracer
    return index

  def print_reverse(self): # Extend print function since we have circular pointer capabilities
    print("Printing linked list (reverse)")
    tracer = self.tail
    index = 0
    if (tracer == None):
      print("Empty list.")
      return -1
    while (tracer != self.head.prev):
      print(f"Index: {index}\t - {tracer.val}")
      tracer = tracer.prev
      index += 1

print("Showing examples for singly linked lists\n");
head = ListHead()
head.print(); # Empty list
head.add(", World");
head.insert("Hello");
head.add("!");
head.print(); # Hello, World!
res = head.remove("Hello");
if (res != -1):
  print(f"Removed item from index {res}\n");
else:
  print("Failed to find item in list\n");

res = head.remove("!");
head.print(); # , World
res = head.remove("????"); # Doesn't exist
head.print(); # , World!

## Same again but with DList/circular

print("\n\n***Showing examples for doubly and circular linked lists***\n");
head = CListHead()
head.print(); # Empty list
head.print_reverse(); # Empty list
head.add(", World");
head.insert("Hello");
head.add("!");
head.print(); # Hello, World !
head.print_reverse(); # , World ! Hello
res = head.remove("Hello");
if (res != -1):
  print(f"Removed item from index {res}\n");
else:
  print("Failed to find item in list\n");

res = head.remove("!");
head.print(); # , World
head.print_reverse(); #, World
res = head.remove("????"); # Doesn't exist
head.print(); # , World!
head.print_reverse(); 

