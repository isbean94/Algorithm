import sys
sys.stdin = open("sample_input.txt")

total_nums = int(input())
for n in range(total_nums):

    N = int(input())
    num_list = list(map(int, input().split()))
    sorted_list = []

    for i in range(10):
        if i % 2:
            sorted_list.append(min(num_list))
            num_list.remove(min(num_list))
        else:
            sorted_list.append(max(num_list))
            num_list.remove(max(num_list))

    str_sorted_list = list(map(str, sorted_list))

    print("#{0} {1}".format(n+1, ' '.join(str_sorted_list)))