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

    def is_prime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def count_primes(self):
        def recursive_count(node):
            if node is None:
                return 0
            if self.is_prime(node.data):
                return 1 + recursive_count(node.next)
            else:
                return recursive_count(node.next)

        return recursive_count(self.head)

# Example usage
dll = DoublyLinkedList()
dll.append(8)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(10)
dll.append(6)
dll.append(7)

print("Count of prime numbers:", dll.count_primes())