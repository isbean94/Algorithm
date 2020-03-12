total_nums = int(input())

for n in range(total_nums):
    N = int(input())
    nums = list(map(int, input().split()))
    max_n = 0
    min_n = 999999

    for num in nums:
        max_n = num if num > max_n else max_n
        min_n = num if num < min_n else min_n

    result = max_n - min_n

    print("#{0} {1}".format(n+1, result))