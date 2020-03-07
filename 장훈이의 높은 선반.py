T = int(input())
for t in range(1, T+1):

    N, B = map(int, input().split())
    people = list(map(int, input().split()))
    result = 999999


    for i in range(1<<N):
        part_sum = 0

        for j in range(N):
            if i & (1<<j):
                part_sum += people[j]
                if part_sum >= result:
                    break

        result = part_sum if B <= part_sum <= result else result

    print("#{0} {1}".format(t, result-B)) 
