T = int(input())
for t in range(1, T+1):

    N = float(input())
    cnt = 0
    result = ''

    while (N != 0) and cnt < 13:
        cnt += 1
        N *= 2

        if N >= 1:
            N -= 1
            result += '1'
        else:
            result += '0'

    if cnt == 13:
        result = 'overflow'

    print("#{0} {1}".format(t, result))