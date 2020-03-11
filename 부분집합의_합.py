import sys
sys.stdin = open("sample_input.txt")

total_nums = int(input())
num_list = list(range(1,13))

for num in range(total_nums):

    N, K = map(int, input().split())
    counter = 0
    n = len(num_list)

    for i in range(1<<n):
        part_list = []
        for j in range(n):
            if i & (1<<j):
                part_list.append(num_list[j])
        if len(part_list) == N and sum(part_list) == K:
            counter += 1
    
    print("#{0} {1}".format(num+1, counter))
            