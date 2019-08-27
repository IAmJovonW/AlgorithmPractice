#Linked List Construction

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
		
		pass
		    
    def setTail(self, node):
        # Write your code here.
		pass
    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
		pass
    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
		pass
    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
		pass
    def removeNodesWithValue(self, value):
        # Write your code here.
		pass
    def remove(self, node):
        # Write your code here.
		if node == self.head:
			node.next = self.head
		elif node == self.tail:
			node.prev = self.tail
		
		self.removeBindings(node)
		
		
    def containsNodeWithValue(self, value):
      # Write your code here.
		node = self.head
		while node is not None and node.value != value:
			node = node.next
		return node is not None
			
	def removeBindings(self, node):
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.next = None
		node.prev = None
		
