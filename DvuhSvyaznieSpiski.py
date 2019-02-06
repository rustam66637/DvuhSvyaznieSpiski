class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val): #метод поиска первого узла по его значению
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val): #метод поиска всех узлов по конкретному значению
        node = self.head
        s = []
        while node is not None:
            if node.value == val:
                s.append(node)
            node = node.next
        return s

    def delete(self, val, all=False): #метод удаления одного\нескольких узла\ов по значению
            node = self.head
            old = self.head
            nxt = self.head
            while node is not None:
                if node.value == val:
                    if node == self.head and node == self.tail and node.value == val: #если в списке один узел
                        self.head = self.tail = None
                        node = old = nxt = None
                        break
                    if node == self.head: #если узел первый
                        node = node.next
                        old = node
                        nxt = node
                        self.head = node
                        node.prev = None
                        continue
                    if node == self.tail: # если узел последний
                        old.next = None
                        self.tail = old
                        return
                    else:
                        old.next = nxt
                        nxt.prev = old
                    if all == False:
                        return
                old = node
                node = nxt
                if nxt.next != None:
                    nxt = nxt.next
                else:
                    return

    def clean(self): #метод очистки всего содержимого
        self.__init__()

    def len(self): #метод вычисления длины списка
        node = self.head
        s = 0
        while node != None:
            s += 1
            node = node.next
        return s

    def insert(self, afterNode, newNode): #метод вставки узла после заданного узла
        if afterNode == None and self.head == None and self.tail == None:
            if type(newNode) == Node:
                LinkedList2.add_in_tail(self, newNode) # проверка на пустой список
            if type(newNode) == int:
                self.tail = self.head = Node(newNode)
            return
        node = self.head
        while True:
            if type(newNode) == Node:
                LinkedList2.add_in_tail(self, newNode)
                return
            if type(newNode) == int and type(afterNode) == Node:
                if node.value == afterNode.value:
                    node.next = Node(newNode, node, node.next)
                    if node.next.next == None:
                        self.tail = node.next
                    break
                else: node = node.next
            if type(newNode) == int and type(afterNode) == int:
                if node.value == afterNode:
                    node.next = Node(newNode, node.next)
                    if node.next.next == None:
                        self.tail = node.next
                    break
                else: node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            item.prev = None
            item.next = None
            self.tail = newNode
        else:
            self.head.prev = newNode
            item.next = self.head
        self.head = newNode
