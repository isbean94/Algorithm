total_nums = int(input())

for n in range(total_nums):

    N = int(input())
    num_list = list(map(int, input().split()))
    danzo = -1

    if N > 1:
        for i in range(N-1):
            for j in range(i+1,N-1):
                sample = num_list[i]*num_list[j]
                if sample > 10:
                    for t in range(len(str(sample))-1):
                        if str(sample)[t] > str(sample)[t+1]:
                            break
                    else:
                        danzo = sample if sample >= danzo else danzo
        
    print('#{0} {1}'.format(n+1, danzo))