# Izvadīs [ 1 2 3 ], ja saistītajā sarakstā ie elementi 1->2->3 un tiek uzsaukta metode print_list() 

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self,value=None):
#         if value is not None:
#             new_node = Node(value)
#             self.head = new_node
#             self.tail = new_node
#             self.length = 1
#         else:
#             self.head = None
#             self.tail = None
#             self.length = 0
    
#     def print_list(self):
#         temp = self.head 
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
    
#     # def make_empty(self):
#     #     self.head = None
#     #     self.tail = None
#     #     self.length = 0
        
#     # def append(self, value):
#     #     new_node = Node(value)
#     #     if self.head is None:
#     #         self.head = new_node
#     #         self.tail = new_node
#     #     else:
#     #         self.tail.next = new_node
#     #         self.tail = new_node
#     #     self.length += 1

# my_linked_list = LinkedList(1)
# my_linked_list.make_empty()

# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)

# print('Linked List:')
# my_linked_list.print_list()

# ________________________________________________________________________________________________
# Izvadīs [ 1 3 ], jasaistītajā sarakstā ie elementi 1->2->3->4 un tiek uzsaukta metode print_list() 

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self,value=None):
#         if value is not None:
#             new_node = Node(value)
#             self.head = new_node
#             self.tail = new_node
#             self.length = 1
    
#     def print_list(self):
#         temp = self.head 
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next.next

#     # def make_empty(self):
#     #     self.head = None
#     #     self.tail = None
#     #     self.length = 0
        
#     # def append(self, value):
#     #     new_node = Node(value)
#     #     if self.head is None:
#     #         self.head = new_node
#     #         self.tail = new_node
#     #     else:
#     #         self.tail.next = new_node
#     #         self.tail = new_node
#     #     self.length += 1

# my_linked_list = LinkedList(1)
# my_linked_list.make_empty()

# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)

# print('Linked List:')
# my_linked_list.print_list()

# ________________________________________________________________________________________________
# Izvadīs [ 1 2 3 4 ], jasaistītajā sarakstā ie elementi 1->2->3->4->5->6->7->8 un tiek uzsaukta metode print_list() 

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self,value):
#             new_node = Node(value)
#             self.head = new_node
#             self.tail = new_node
#             self.length = 1
    
#     def print_list(self):
#         temp = self.head 
#         count = 0
#         while temp is not None and count < 4:
#             print(temp.value)
#             temp = temp.next
#             count +=1

#     # def make_empty(self):
#     #     self.head = None
#     #     self.tail = None
#     #     self.length = 0
        
#     # def append(self, value):
#     #     new_node = Node(value)
#     #     if self.head is None:
#     #         self.head = new_node
#     #         self.tail = new_node
#     #     else:
#     #         self.tail.next = new_node
#     #         self.tail = new_node
#     #     self.length += 1

# my_linked_list = LinkedList(1)
# my_linked_list.make_empty()

# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)
# my_linked_list.append(6)
# my_linked_list.append(7)
# my_linked_list.append(8)

# print('Linked List:')
# my_linked_list.print_list()

# ________________________________________________________________________________________________
# Izvadīs [ 3 ], jasaistītajā sarakstā ie elementi 1->2->3->4->5 un tiek uzsaukta metode print_list() 

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self,value=None):
#         if value is not None:
#             new_node = Node(value)
#             self.head = new_node
#             self.tail = new_node
    
#     def print_list(self):
#         slow = self.head
#         fast = self.head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         print(slow.value)

#     # def make_empty(self):
#     #     self.head = None
#     #     self.tail = None
#     #     self.length = 0
        
#     # def append(self, value):
#     #     new_node = Node(value)
#     #     if self.head is None:
#     #         self.head = new_node
#     #         self.tail = new_node
#     #     else:
#     #         self.tail.next = new_node
#     #         self.tail = new_node
#     #     self.length += 1

# my_linked_list = LinkedList(1)
# my_linked_list.make_empty()

# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)

# print('Linked List:')
# my_linked_list.print_list()

# ________________________________________________________________________________________________
# Kādu komandu jāizmanto, lai pievienotu ērtību 5 rindai, izmantojot QUEUE klase?

# class Queue:
#     def __init__(self):
#         self.items = []

#     # Добавление элемента 
#     def enqueue(self,item):
#         self.items.append(item)
    
#     # метод отвечает за извлечение (и возвращение) первого элемента из очереди (queue)
#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
        
#     # используется для проверки, содержит ли очередь элементы или нет
#     def is_empty(self):
#         return len(self.items) == 0
    
#     # def __str__(self):
#     #     return str(self.items)

# q = Queue()
# q.enqueue(5)
# print(q)

# _______________________________________________________________
#  JAUTAJUMI

# 1.  Ja masīva sākuma adrese ir 1000, katrs elements aizņem 8 baitus un pirmā elementa indekss ir 0, kāda ir 6.elementa adrese? 
# -> 1048

# 2. Kāds būs masīva saturs pēc šādas programmas izpildes?
# -> 10 30 20 0 0 40

# a=[10,30,20,10,30,40]
# for i in range(len(a)):
#     for j in range (i+1, len(a)):
#         if a[i] == a[j]:
#             a[j] =0
# print(a)

# 3. Kura datu struktūra ir vispiemērotākā UNDO darbībai sistēmā WINDOWS?
# -> Steks

# 4. Dots vienkāršsaistīts saraksts. Kā izskatās šis saraksts pēc elementa 38 pievienošanās head daļā?
# -> 38-74-71

# 5. Ko dara dequeue rindas kontekstā?
# -> Atgriež vērtību un dzēš vērtību

# Kura no dotajām datu struktūrām būs visatbilstošākā, ja nepieciešams piekļūt elementiem pēc pozīcijas ar 0(1) laiku?
# -> Masīvs

# Kura no dotajām datu struktūrām būs visatbolstošākā, ja nepieciešams ielikt elementu vidū ar laiku 0(1)?
# -> Saraksts

# -> Saistīts saraksts