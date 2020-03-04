for t in range(1,int(input())+1):

    N = int(input())
    M = N//2
    square = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                square[i][j], square[j][i] = 0, square[i][j]+square[j][i]

    check = [1]*N
    result = 999999

    def taste(arr1, arr2):

        taste1 = taste2 = 0

        for i in range(M):
            for j in range(i+1,M):
                taste1 += square[arr1[i]][arr1[j]]
                taste2 += square[arr2[i]][arr2[j]]

        return abs(taste1 - taste2)
        

    def part_div(arr1=[],arr2=[],a=0):
        global result

        if len(arr1) == M:

            arr2 = arr2 + list(range(a,N))
            p_result = taste(arr1,arr2)

            result = p_result if p_result <= result else result
            return

        w = []

        for v in range(a,N):
            if check[v]:
                
                check[v] = 0
                part_div(arr1+[v],arr2+w,v+1)
                check[v] = 1

            w.append(v)

    part_div()

    print("#{0} {1}".format(t, result))