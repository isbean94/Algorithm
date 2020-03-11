import sys
sys.stdin = open("sample_input.txt")

total_nums = int(input())

for n in range(total_nums):
    N = int(input())
    white = [[0]*10 for _ in range(10)]
    counter = 0

    for i in range(N):
        x_s, y_s, x_e, y_e, color  = map(int, input().split())
        for y in range(y_s, y_e+1):
            for x in range(x_s, x_e+1):
                if white[x][y] == color or white[x][y] == 3:
                    continue
                else:
                    white[x][y] += color

    for j in range(10):
        counter += white[j].count(3)

    print("#{0} {1}".format(n+1, counter))