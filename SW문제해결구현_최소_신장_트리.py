import heapq

T = int(input())
for t in range(1,T+1):

    V, E = map(int, input().split())
    graph = {}

    for i in range(E):
        s, e, l = map(int, input().split())
        
        if s in graph:
            graph[s].append((l,e))
        else:
            graph[s] = [(l,e)]

        if e in graph:
            graph[e].append((l,s))
        else:
            graph[e] = [(l,s)]

    pq = []
    visit = [0]*(V+1)

    visit[0] = 1
    for sell in graph[0]:
        heapq.heappush(pq, sell)

    result = 0

    while pq:

        n, m = heapq.heappop(pq)
        
        if visit[m]:
            continue
        else:
            visit[m] = 1
            result += n

            for sell in graph[m]:
                heapq.heappush(pq, sell)

    # V, E = map(int, input().split())
    # node = [list(map(int, input().split())) for _ in range(E)]

    # node.sort(key=lambda x: x[2])

    # cnt = 0
    # result = 0
    # visit = [0]*(V+1)

    # while cnt < V:
    #     s, e, l = node.pop(0)
        
    #     if visit[s] and visit[e]:
    #         continue
    #     else:
    #         visit[s] = 1
    #         visit[e] = 1
    #         result += l
    #         cnt += 1

    print("#{0} {1}".format(t, result))