T = int(input())
for t in range(1, T+1):

    N = int(input())

    bill = [tuple(map(int, input().split())) for _ in range(N)]

    bill = sorted(bill, key = lambda x : (x[1], x,[0]))

    result = 1

    v = bill.pop(0)

    while bill:

        w = bill.pop(0)

        if v[1] == w[1]:
            continue
        else:
            if w[0] <  v[1]:
                continue
            else:
                v = w
                result += 1

    print("#{0} {1}".format(t, result))