# T = int(input())
# for t in range(1,T+1):

N, X = input().split()
x_num = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
result = []

for i in X:
    num = x_num[i] if i in x_num else int(i)
    b_num = ''
    d = 8

    while d:
        b_num += str(num//d)
        num = num % d
        d = d // 2

    result.append(b_num)

print(''.join(result))
# print("#{0} {1}".format(t, ''.join(result)))