T = int(input())
for t in range(1, T+1):

    V, E = map(int, input().split())
    graph = {}
    for dot in range(1, V+1):
        graph[dot] = []

    for bar in range(E):
        a, b =  map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    start, end = map(int, input().split())
    goal = False
    q = [(start, 0)]
    visited = {start}

    while q:
        v, d = q.pop(0)

        for w in graph[v]:

            if w == end:
                goal =True
                d += 1
                break
            
            else:
                if w in visited:
                    continue
                else:
                    visited.add(w)
                    q.append( (w, d+1) )
        
        if goal:
            break

    else:
        d = 0

    print("#{0} {1}".format(t, d))