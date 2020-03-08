for t in range(1,int(input())):

    N = int(input())
    score_list = list(map(int,input().split()))
    score_set = set()

    for i in range(1<<N):
        part_sum = 0
        for j in range(N):
            if i & (1<<j):
                part_sum += score_list[j]
        score_set.add(part_sum)

    print("#{0} {1}".format(t, len(score_set)))