T = int(input())
for t in range(1, T+1):

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = {}

    for i in range(0, 2*N, 2):
        if arr[i] in tree:
            tree[arr[i]].append(arr[i+1])
        else:
            tree[arr[i]] = [arr[i+1]]

    result = 1
    q = [M]

    while q:
        v = q.pop(0)

        if v in tree:
            for w in tree[v]:
                q.append(w)
                result += 1

    print("#{0} {1}".format(t, result))