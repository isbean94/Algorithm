T = int(input())
for t in range(1,T+1):
    
    N = int(input())
    bus_stop = {key : 0 for key in range(1,5001)}
    
    for n in range(N):
        A,B = map(int, input().split())
        for s in range(A,B+1):
            if s in bus_stop:
                bus_stop[s]  += 1

    C = int(input())
    bus = []
    for c in range(C):
        bus.append(str(bus_stop[int(input())]))
    
    print("#{0} {1}".format(t, ' '.join(bus)))