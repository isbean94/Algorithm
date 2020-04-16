T = int(input())
for t in range(1, T+1):

    N, M, L = map(int, input().split())
    tree = [0]*(N+1)

    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val

    def tree_add(node):
        if tree[node]:
            pass
        else:
            if (N % 2) == 0 and node == M:
                tree[node] = tree_add(node*2)
            else:
                tree[node] = tree_add(node*2) + tree_add((node*2)+1)
            
        return  tree[node]

    result = tree_add(L)

    print("#{0} {1}".format(t, result))