# T = int(input())
# for t in range(1,T+1):

#     N, M = map(int, input().split())
#     mylist = list(map(int, input().split()))

#     for i in range(1,M):
#         newlist = list(map(int, input().split()))

#         for idx,data in enumerate(mylist):
#             if newlist[0] < data:
#                 mylist = mylist[:idx] + newlist + mylist[idx:]
#                 break
#         else:
#             mylist = mylist + newlist

#     print("#{0} {1}".format(t, ' '.join(map(str, reversed(mylist[-10:])))))


class Node:
    def __init__(self, d, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def resultList(lst, arr):
    i = 0
    p = lst.tail

    while i < 10:
        arr.append(p.data)
        p = p.prev
        i += 1

def makeList(lst, new):
    if lst.head == None:
        lst.head = lst.tail = new
    else:
        lst.tail.next = new
        new.prev = lst.tail
        lst.tail = new

def insertAt(lst, new):
    pre, cur = None, lst.head
    
    while cur:
        if cur.data > new.head.data:
            if pre:
                pre.next = new.head
                new.head.prev = pre

                cur.prev = new.tail
                new.tail.next = cur

            else:
                lst.head = new.head

                cur.prev = new.tail
                new.tail.next = cur
            break
        pre = cur
        cur = cur.next
    else:
        pre.next = new.head
        new.head.prev = pre

        lst.tail = new.tail


T = int(input())
for t in range(1, T+1):

    N, M= map(int, input().split())

    mylist = LinkedList()

    for i in list(map(int, input().split())):
        makeList(mylist, Node(i))

    for m in range(1, M):
        newlist = LinkedList()
        for n in list(map(int, input().split())):
            makeList(newlist, Node(n))
            
        insertAt(mylist, newlist)

    result = []
    resultList(mylist, result)

    print("#{0} {1}".format(t, ' '.join(map(str, result))))