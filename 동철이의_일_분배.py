for t in range(1,int(input())+1):
    print("#{0}".format(t),end=' ')

    N = int(input())
    square = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]

    check = [1]*N
    pws_list = []
    max_result = 0

    def pws(arr=[], row=0, result=100):
        global max_result

        if len(arr) == N:
            max_result = result
            return 

        for i in range(N):
            if check[i] and (result*square[row][i] > max_result):
                check[i] = 0
                pws(arr+[i], row+1, result*square[row][i])
                check[i] = 1

    pws()

    # for sample in pws_list:
    #     result = 100
    #     for idx, val in enumerate(sample):
    #         result = result*square[idx][val]
    #     max_result = result if result >= max_result else max_result

    print(format(max_result,".6f"))