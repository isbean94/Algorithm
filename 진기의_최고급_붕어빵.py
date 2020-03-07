import sys
sys.stdin = open("input.txt")

total_num = int(input())
for n in range(total_num):

    N, M, K = map(int, input().split())
    guests = list(sorted(map(int, input().split())))
    time_attack = 0
    bung_u = 0
    timer = 0
    result = 'Possible'

    while N > 0:
        if guests[0] == 0:
            result = 'Impossible'
            break

        timer += 1
        if timer == M:
            timer = 0
            bung_u += K

        time_attack += 1
        if time_attack == guests[0]:
            guest = guests.count(guests[0])
            del guests[:guest]
            bung_u -= guest
            N -= guest

        if bung_u < 0:
            result = 'Impossible'
            break

    print('#{0} {1}'.format(n+1, result))