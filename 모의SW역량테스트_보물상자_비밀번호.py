T = int(input())
for t in range(1, T+1):

    N, K = map(int, input().split())
    R = N//4
    password = input()
    part_pw = set()

    for n in range(R):
        r_password = password[n:] + password[:n]
        part_pw.update( [ r_password[:R], r_password[R:R*2], r_password[R*2:R*3], r_password[R*3:R*4] ] )

    part_pw = list(reversed(sorted(list(map(lambda x: int('0x' + x, 16), part_pw)))))

    print("#{0} {1}".format(t,part_pw[K-1]))