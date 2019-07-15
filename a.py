# class student(object):
#     def __init__(me, name, age):
#         me.name = name
#         me.age = age

#     def __str__(self):
#         return "I am " + self.name + " and I am " +  str(self.age) + " years old."

#     def __len__(self):
#         return self.age
    
#     def __add__(self, other):
#         self.name = self.name + other.name
#         self.age = self.age + other.age
#         return self




# class LL:
#     def __init__(self):
#         self.root = None

#     def printf(self):
#         current = self.root
#         while(current!=None):
#             print(current.value)
#             current = current.next

#     def insert(self, value):
#         pass


# linked_list = LL()
# linked_list.insert('adasd')
# # root = Node('adadasd')
# # root.next = Node(12)
# # root.next.next = Node(13)
# # root.printf()

# babu = student("babu", 0)
# sangam = student("sangam", -1)
# print(sangam+babu)
# # print(len(student("babu", 12)))


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None




# class LL:
#     def __init__(self):
#         self.head=None

#     def node(self, value):
#         self.value = value
#         self.next = None
#         return self


#     def insert(self, value):
#         node=self.node(value)
#         node.next=self.head
#         self.head=node


#     def print(self):
#         temp=self.head
#         while(temp):
#             print(temp.value)
#             temp=temp.next


# class LL:
#     def __init__(self):
#         self.head = None
#         # self.next = insert(value)

#     def insert(self, value):
#         self.value = LL(value)
#         self.value.next = None



# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class LL:
#     def __init__(self):
#         self.head = None

#     def insert(self, value):
#         if self.head == None:
#             self.head = Node(value)
#             return
#         else:
#             tmp = self.head
#             if value <= tmp.value:
#                 newnode = Node(value)
#                 newnode.next = self.head
#                 self.head = newnode
#                 return
#             else:
#                 while tmp.next and tmp.next.value < value:
#                     tmp = tmp.next
#                 prev = tmp
#                 nex = prev.next
#                 newnode = Node(value)
#                 prev.next = newnode
#                 newnode.next = nex
#                 return

    # def print(self):
    #     tmp = self.head
    #     while tmp:
    #         print(tmp.value)
    #         tmp = tmp.next
    #     return




# class Student:
#     def __init__(self, name, age):
#         print(self)
#         self.name = name
#         self.age = age

# n=[1,3,5,2,6,32]
# ll = LL()
# for i in range(len(n)):
#     ll.insert(n[i])
# ll.print()


# student = Student("babu", 20)
# student.id = 123
# print(student.name, student.age, student.id)
# student2 = Student("baby", 30)
# student2.id = 123

# print(Student.mro())



# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None

# class dll:
#     def __init__(self):
#         self.head=None
#         self.tail=None

#     def insert(self, value):
#         if self.head==None:
#             self.head=Node(value)
#             self.tail=self.head

#         else:
#             tmpf = self.head
#             tmpb = self.tail
#             if value <= tmpf.value:
#                 newnode=Node(value)
#                 newnode.next=self.head
#                 self.head.prev=newnode
#                 self.head=newnode
#                 return

#             else:
#                 while tmpf.next and tmpf.next.value < value:
#                     tmpf = tmpf.next
#                 newnode = Node(value)
#                 newnode.next = tmpf.next
#                 newnode.prev = tmpf
#                 if tmpf.next==None:
#                     self.tail = newnode
#                 else:
#                     tmpf.next.prev = newnode
#                 tmpf.next = newnode
#                 return

#     def print(self):
#         tmp = self.head
#         while tmp:
#             print(tmp.value)
#             tmp = tmp.next
#         return



# n=[1,3,5,2,6,32]
# ll = dll()
# for i in range(len(n)):
#     ll.insert(n[i])
# print(ll.head.value)
# print(ll.head.next.value)
# print(ll.head.next.next.next.value)


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# class tree:
#     def __init__(self):
#         self.start=None

#     def insert(self, value):
#         if self.start==None:
#             self.start = Node(value)

#         else:
#             tmp = self.start
#             while tmp:
#                 if value <= tmp.value:
#                     if tmp.left == None:
#                         tmp.left = Node(value)
#                         return
#                     else:
#                         tmp=tmp.left
#                 else:
#                     if tmp.right == None:
#                         tmp.right = Node(value)
#                         return
#                     else:
#                         tmp=tmp.right

#     def print(self):
#     	r = self.start
    	


#     	def traverse(root):
#     		if(root==None):
#     			return
#     		traverse(root.left)
#     		print(root.value)
#     		traverse(root.right)
#     		return
    	

#     	traverse(r)


# n=[6,1,3,5,2,7,32]
# tr = tree()
# for i in range(len(n)):
#     tr.insert(n[i])
# print(tr.start.value)
# print(tr.start.left.right.value)
# tr.print()




class Node:
    def __init__(self):
        self.value = [None]*26
        self.end = False

class trie:
    def __init__(self):
        self.start = Node()

    def numb(self, num, n):
        for i in range (len(str(num))-n):
        	num = num/10
        return (num%10)

    def insert(self, value):
        temp = self.start
        for i in range (len(str(value)):
            indx = self.numb(value, i)
            if not temp.value[indx]:
                temp.value[indx] = Node()
            temp = temp.value[indx]
        temp.end = True


n=[6,1,3,5,2,7,32]
tr = trie()
for i in range(len(n)):
    tr.insert(n[i])
print(tr.start)