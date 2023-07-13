class Node:
	head = None
	ishead = False
	def __init__(self, value=0, next=None):
		self.value = value
		self.next = next
		
		if Node.ishead == False:
			Node.head = self
			Node.ishead = True

class LinkedList:
	def __init__(self):
		self = Node.head
		print(self)

def getItemNum(head, n):
	current = head
	for i in range(n):
		if current.value == n:
			return current
		else:
			current = current.next
	return 

def getItemIndex(head, n):
	current = head
	i = 0
	while i <= n:
		if current == None: break
		elif i == n: return current
		else: current = current.next
		i+=1
	return 

if __name__ == "__main__":
	h = Node("h")
	h.value = "head"
	s = Node("s")
	s.value = "second"
	t = Node("t")
	t.value = "third"
	h.next = s
	s.next = t

	print(getItemIndex(h,3).value)