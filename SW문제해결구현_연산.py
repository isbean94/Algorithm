from collections import deque

T = int(input())
for t in range(1, T+1):

    N, M = map(int, input().split())

    cnt = 0
    q = deque([(N,cnt)])
    visit = [0]*1000001

    while q:
        x, y = q.popleft()

        if x == M:
            result = y
            break
        
        elif x < 0:
            continue

        elif x > 1000000:
            continue
        
        elif visit[x]:
            continue

        else:
            visit[x] = 1
            y += 1

            for i in range(4):
                if i == 0:
                    q.append( (x+1, y) )
                elif i == 1:
                    q.append( (x-1, y) )
                elif i == 2:
                    q.append( (x*2, y) )
                elif i == 3:
                    q.append( (x-10, y) )

    print("#{0} {1}".format(t, result))