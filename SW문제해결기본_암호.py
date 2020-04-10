class Node:
    def __init__(self, d, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

def resultList(lst, arr):  # 연결리스트 출력    
    p = lst.tail
    for _ in range(lst.size):
        arr.append(p.data)
        p = p.prev  # 노드들을 순차 탐색

def makeList(lst, new):
    if lst.head == None:
        lst.head = new
        lst.tail = new
        new.prev = new
        new.next = new
    else:
        lst.head.prev = new
        lst.tail.next = new
        new.prev = lst.tail
        new.next = lst.head
        lst.tail = new     
    lst.size += 1    

def insertAt(lst, idx, rot):
    pre, cur = lst.tail, lst.head

    for _ in range(rot):

        for _ in range(idx):
            pre = cur
            cur = cur.next
        
        new = Node( pre.data + cur.data )
        
        if pre.next == lst.head:
            lst.tail = new
        elif cur.prev == lst.tail:
            lst.head = new

        pre.next = new
        new.prev = pre
        cur.prev = new
        new.next = cur

        pre, cur =  new.prev, new
        lst.size += 1
        

T = int(input())
for t in range(1, T+1):

    N, M, K = map(int, input().split())
    in_list = list(map(int, input().split()))

    mylist = LinkedList()

    for i in in_list:
        makeList(mylist, Node(i))

    insertAt(mylist, M, K)

    result = []
    resultList(mylist, result)

    print("#{0} {1}".format(t, ' '.join(map(str, result[:10]))))