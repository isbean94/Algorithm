T = int(input())
for t in range(1,T+1):

    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    # 나머지 정리 #

    # remain = M % N

    # result = num_list[remain]

    # print(result)

    # Queue #

    for _ in range(M):
        v = num_list.pop(0)
        num_list.append(v)

    result = num_list[0]

    print("#{0} {1}".format(t, result))
