T = int(input())
for t in range(1, T+1):

    D, M, M3, Y = map(int, input().split())
    schedule = list(map(int, input().split()))

    for i in range(12):
        
        if schedule[i]*D >= M:
            schedule[i] = M
        
        else:
            schedule[i] = schedule[i]*D

    print(schedule)

    total_fee = []

    def bill(arr=[],mid_fee=0):

        for i in range(10):

            part_fee = schedule[i] + schedule[i+1] + schedule[i+2]
            
            if (part_fee >= M3):
                arr.append(i)
        
        if len(arr) == 0:
            total_fee.append(mid_fee+sum(schedule))
            return

        for i in arr:
            a, b, c = schedule[i], schedule[i+1], schedule[i+2]
            schedule[i], schedule[i+1], schedule[i+2] = 0, 0, 0
            bill([], mid_fee + M3)
            schedule[i], schedule[i+1], schedule[i+2] = a, b, c

    bill()

    result_fee = min(total_fee) if min(total_fee) <= Y else Y 

    print("#{0} {1}".format(t, result_fee))