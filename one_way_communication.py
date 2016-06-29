class Node:
  def __init__(self,position,next=None):
    self.position = position
    self.next = next
  def __str__(self):
    return repr(self.position)

class LinkedList:
  def __init__(self):
    self.reference = None
  def prepend(self,position):
    if not self.reference:
      self.reference = Node(position)
    else:
      cur = self.reference
      new_node = Node(position)
      new_node.next = cur
      self.reference = new_node
  def append(self,position):
    if not self.reference:
      self.reference = Node(position)
    else:
      cur = self.reference
      while cur.next:
        cur = cur.next
      new_node = Node(position)
      cur.next = new_node
  def insert(self,position,talks_to):
    cur = self.reference
    while cur.next.position != talks_to and cur != None:
      cur = cur.next
    if cur:
      new_node = Node(position)
      talking_to = cur.next 
      cur.next = new_node
      new_node.next = talking_to
    else:
      self.append(position)
      self.append(talks_to)
  def pprint(self):
    cur = self.reference
    while cur:
      print(cur,end="->")
      cur = cur.next

if __name__ == '__main__':
  one_way_communication = LinkedList()
  one_way_communication.prepend("Eric")
  one_way_communication.append("Mark")
  one_way_communication.insert("Sarah","Mark")
  one_way_communication.pprint()
