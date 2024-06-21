class Node:
    def __init__(self):
        self.d = {}     
        self.flag = 0   

class Tries:
    def __init__(self):
        self.root = Node()  
    
    def insert(self, word):
        t = self.root
        for char in word:
            if char not in t.d:
                t.d[char] = Node()  
            t = t.d[char]
        t.flag = 1  
    
    def search_word(self, word):
        t = self.root
        for char in word:
            if char not in t.d:
                return False
            t = t.d[char]
        return t.flag == 1  
    
    def search_prefix(self, prefix):
        t = self.root
        for char in prefix:
            if char not in t.d:
                return False
            t = t.d[char]
        return True  

    def _collect_words(self, node, prefix):
        words = []
        if node.flag == 1:
            words.append(prefix) 
        for char, next_node in node.d.items():
            words.extend(self._collect_words(next_node, prefix + char))  
        return words
    
    def get_words_with_prefix(self, prefix):
        t = self.root
        for char in prefix:
            if char not in t.d:
                return []  
            t = t.d[char]
        return self._collect_words(t, prefix)
    
t1 = Tries()


t1.insert("school")
t1.insert("world")
t1.insert("word")
t1.insert("scholar")


print(t1.search_word("word"))  
print(t1.search_word("wood")) 

print(t1.search_prefix("sch"))  
print(t1.search_prefix("wor")) 
print(t1.search_prefix("abc"))  

print(t1.get_words_with_prefix("sch"))  
print(t1.get_words_with_prefix("wor"))  
print(t1.get_words_with_prefix("abc"))  