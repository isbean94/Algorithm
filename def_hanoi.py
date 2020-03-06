# def hanoi(n, a, b, c):
#     if n == 1:
#         print('{0}을 {1}에서 {2}로 옮깁니다.'.format(n, a, c))
#     else:
#         hanoi(n-1, a, c, b)
#         print('{0}을 {1}에서 {2}로 옮깁니다.'.format(n, a, c))
#         hanoi(n-1, b, a, c)

# hanoi(5, 'a', 'b', 'c')

x = a = [5, 4, 3, 2, 1]
y = b = []
z = c = []

def hanoi(n, a, b, c):
    if n == 1:
        m = a.pop()
        c.append(m)
        print(x, y, z)
    else:
        hanoi(n-1, a, c, b)
        m = a.pop()
        c.append(m)
        print(x, y, z)
        hanoi(n-1, b, a, c)

hanoi(5, a, b, c)