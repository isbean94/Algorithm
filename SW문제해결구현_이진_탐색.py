T = int(input())
for t in range(1, T+1):

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    l = 0
    r = N-1

    def search(l, r, num, check):
        if (l > r):
            return False

        m = (l+r)//2

        if (num == A[m]):
            return True
        else:

            if num > A[m]:
                if check == 1:
                    return False
                return search(m+1, r, num, 1)
            elif num < A[m]:
                if check == 0:
                    return False
                return search(l, m-1, num, 0)

    result = 0

    for num in B:
        if search(l, r, num, -1):
            result += 1

    print("#{0} {1}".format(t, result))