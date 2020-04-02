T = int(input())
for t in range(1,T+1):

    N, M = map(int, input().split())
    pizza_dict = dict(zip(range(1,M+1), map(int, input().split())))

    q_oven = list(range(1,N+1))

    while len(q_oven) > 1:
        i = q_oven.pop(0)
        if pizza_dict[i] == 1: 
            if N < M:
                N += 1
                q_oven.append(N)
        else:
            q_oven.append(i)
            pizza_dict[i] = int(pizza_dict[i]//2)
    
    print("#{0} {1}".format(t, q_oven[0]))