class Node:
    def __init__(self, d, n=None):
        self.data = d
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def resultList(lst, arr):  # 연결리스트 출력
    p = lst.head
    while p:
        arr.append(p.data)
        p = p.next  # 노드들을 순차 탐색

def makeList(lst, new):
    if lst.head == None:
        lst.head = lst.tail = new
    else:
        lst.tail.next = new
        lst.tail = new

def insertAt(lst, idx, new):
    pre, cur = None, lst.head
    
    for _ in range(idx):
        pre = cur
        cur = cur.next
    
    new.next = cur
    if pre:
        pre.next = new
    else:
        lst.head = new

T = int(input())
for t in range(1, T+1):

    N, M, L = map(int, input().split())
    in_list = list(map(int, input().split()))

    mylist = LinkedList()

    for i in in_list:
        makeList(mylist, Node(i))


    for _ in range(M):
        idx, new = map(int, input().split())
        insertAt(mylist, idx, Node(new))


    result = []
    resultList(mylist, result)

    print("#{0} {1}".format(t, result[L]))