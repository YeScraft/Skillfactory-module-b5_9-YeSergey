class Node(object): # создаёт узел
    def __init__(self, value=None, next=None):
        self.value = value
        self.next  = next

    def __str__(self):
        return str(self.value)

    def print_reverse_node(self):
        if self.next != None:
            tail = self.next
            tail.print_reverse_node()
        print (self.value, end = " ")

class LinkedList(): # создает связный список
    def __init__(self):
        self.length = 0
        self.head = None
    
    def print_list(self): # печатает связный список
        if self.head is None:
            print("[]")
        else:
            print("[", end = " ")
            head = self.head
            print(head, end = " ")
            while head.next:         
                head = head.next
                print(head, end = " ")
            print("]")

    def print_reverse_list(self): # печатает связный список в обратном порядке
        print ("[", end = " ")
        if self.head != None:
            self.head.print_reverse_node()
        print ("]")

    def add_first(self, value): # добавляет узел к началу связного списка
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def append_node(self, value): # добавляет узел в конец связного списка
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                self.length += 1
            # elif self.head.next is None:
            #     self.head.next = new_node
            #     new_node.next = None
            #     self.length += 1
            else:
                node = self.head
                while node.next:
                    node = node.next
                node.next = new_node
                self.length += 1
                #print(node, self.length)

    def reverse_linked_list(self): # разворачивает связный список
        r_list = LinkedList()
        node = self.head
        r_list.add_first(node.value)
        while node.next:
            r_list.add_first(node.next.value)
            node = node.next
        self.head = r_list.head
        return self

    def remove_duplicates(self): # удаляет из связного списка не уникальные значения
        values_list = []
        duplicates_list = []
        node = self.head
        values_list.append(node.value)
        while node.next:
            node = node.next
            if node.value in values_list: duplicates_list.append(node.value)
            values_list.append(node.value)
        if duplicates_list:   
            i = 1 
            while i <= self.length:
                node = self.head
                if self.head.value in duplicates_list and node.next is not None:
                    node = self.head.next
                    self.head = node
                elif self.head.value in duplicates_list and node.next is None:
                    print("Список состоял из дубликатов")
                    self.head = None
                else:
                    while node.next:
                        if node.next.value in duplicates_list:
                            node.next = node.next.next
                        else:
                            node = node.next
                i+=1

    def give_kth_last(self, k): # возвращает k-й элемент с конца связного списка
        n = self.length - k
        print("k: ", k)
        if n == 0 or n == self.length:
            return self.head
        elif n < 0:
            k = k % self.length
            n = abs(self.length - k)
            node = self.head
            i = 1
            while i <= (n):
                node = node.next
                i+=1
            second = node
            return second
        elif n > self.length:
            n = n % self.length
            node = self.head
            i = 1
            while i <= (n):
                node = node.next
                i+=1
            second = node
            return second
        else:
            node = self.head
            i = 1
            while i <= (n):
                node = node.next
                i+=1
            second = node
            return second



linkedlist = LinkedList()

q = 12

w = "w"

linkedlist.add_first(9)
linkedlist.add_first(8)
linkedlist.add_first(7)
linkedlist.add_first(6)
linkedlist.add_first(5)
linkedlist.add_first(4)
linkedlist.add_first(3)
linkedlist.add_first(2)
linkedlist.add_first(1)
# linkedlist.add_first("a")
# linkedlist.add_first("a")
# linkedlist.add_first(2)
# linkedlist.add_first(2)
# linkedlist.add_first(4)
# linkedlist.add_first("s")
# linkedlist.add_first(7)
# linkedlist.add_first(3)
# linkedlist.add_first(3)
# linkedlist.add_first(3)
# linkedlist.add_first(q)
# linkedlist.add_first(w)
# linkedlist.add_first(8)
# linkedlist.add_first(7)
# linkedlist.add_first(11)
# linkedlist.add_first(11)
# linkedlist.add_first(11)

linkedlist.print_list()

#linkedlist.remove_duplicates()

#linkedlist.reverse_linked_list()

kth_last = linkedlist.give_kth_last(0)

#kth_last.print_list()

print("kth_last: ", kth_last)

#linkedlist.print_list()

#linkedlist.print_reverse_list()

# linkedlist2 = LinkedList()

# linkedlist2.append_node(111)
# linkedlist2.append_node(222)
# linkedlist2.append_node(333)
# # linkedlist2.append_node(444)

# linkedlist2.print_list()

# print(linkedlist2.head.next)
