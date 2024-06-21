class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def even_odd_sum_difference(self):
        def recursive_sum(node):
            if node is None:
                return 0, 0  # Even sum, Odd sum

            even_sum, odd_sum = recursive_sum(node.next)

            if node.data % 2 == 0:
                even_sum += node.data
            else:
                odd_sum += node.data

            return even_sum, odd_sum

        even_sum, odd_sum = recursive_sum(self.head)
        return even_sum - odd_sum

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)

print("Difference between sum of even and odd numbers:", dll.even_odd_sum_difference())