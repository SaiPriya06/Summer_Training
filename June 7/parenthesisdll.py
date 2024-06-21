class Node:
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data, pos):
        new_node = Node(data, pos)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop(self):
        if not self.tail:
            return None
        popped_node = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return popped_node

def is_valid_parentheses(s):
    stack = DoublyLinkedList()
    mapping = {')': '(', '}': '{', ']': '['}
    for i, char in enumerate(s):
        if char in mapping.values():
            stack.append(char, i)
        elif char in mapping.keys():
            last = stack.pop()
            if not last or last.data != mapping[char]:
                return f"Unbalanced at position {i}"
    if stack.head:
        return f"Unbalanced at position {stack.head.pos}"
    return "valid"

# Example usage with input string
input_string = input("Enter a string with parentheses: ")
result = is_valid_parentheses(input_string)
print(result)