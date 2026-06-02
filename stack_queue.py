class Stack:
  def __init__(self):
    self.daftar_item = []
    
  def push(self, item):
    self.daftar_item.append(item)

  def pop (self):
    if self.daftar_item:
      return self.daftar_item.pop(0)

  def display(self):
    return self.daftar_item

class Queue:
  def __init__(self):
    self.daftar_item = []

  def enqueue(self, item):
    self.daftar_item.append(item)

  def dequeue(self):
    if self.daftar_item:
      return self.daftar_item.pop(0)

  def display(self):
    return self.daftar_item
