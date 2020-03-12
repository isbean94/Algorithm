total_nums = int(input())

for n in range(total_nums):
    K, N, M = map(int, input().split())
    station_list = [0]*(N+1)
    charge_station = list(map(int, input().split()))
    for i in charge_station:
        station_list[i] = 1

    charge_counter = 0


    # now_station = 0    
    # second_break = 0

    # while now_station + K < N:    
    #     for j in range(K, 0, -1):
    #         if station_list[now_station+j]:
    #             charge_counter += 1
    #             now_station += j
    #             second_break = 1
    #             break

    #     if second_break:
    #         second_break = 0
    #         continue

    #     charge_counter = 0
    #     break
        
    # print("#{0} {1}".format(n+1, charge_counter))


    pass_counter = 0

    for i in range(N+1):
        if pass_counter:
            pass_counter -= 1
            continue

        if i+K >= N:
            break

        for j in range(K, 0, -1):
            if station_list[i+j]:
                charge_counter += 1
                pass_counter += j-1
                break

        if pass_counter:
            continue

        charge_counter = 0
        break

    print("#{0} {1}".format(n+1, charge_counter))