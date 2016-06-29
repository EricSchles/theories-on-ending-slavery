#The social graph

The idea for a set of data structures to understand and model power came to me from the implicit picture drawn in [this wonderful articile](https://www.newscientist.com/article/mg22329850-600-end-of-nations-is-there-an-alternative-to-countries/?utm_source=NSNS&utm_medium=SOC&utm_campaign=hoot&cmpid=SOC%7CNSNS%7C2016-GLOBAL-hoot).  In case the article has been removed, taken down or the link has simply disappeared, I have copied it's contents [here](End_of_nations_Is_there_an_alternative_to_countries.txt).  You're far better off reading from the link than my copied version, it only has the text.

So how does one model control structures programmatically?

It turns out to be quiet simple.  Let's take the idea of a linked list and think about what sort of control structure that would yield:

(The following is written in Python3.5.1)
```
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
    if not self.refernece:
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
    cur = self.refernece
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

if __name__ == '__main__':
  one_way_communication = LinkedList()
  one_way_communication.prepend("Eric")
  one_way_communication.append("Mark")
  one_way_communication.insert("Sarah","Mark")
  one_way_communication.pprint()
```
      
