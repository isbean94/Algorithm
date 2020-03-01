T = int(input())
for t in range(1,T+1):

    N = int(input())
    cal_num = list(map(int, input().split()))
    cal = ['+', '-', '*', '/']
    numbers = list(map(int, input().split()))

    cal_part = set()

    def ps(arr=[]):

        if len(arr) == (N-1):
            cal_part.add(tuple(arr))
            return

        for idx, val in enumerate(cal):

            if cal_num[idx]:
                cal_num[idx] -= 1
                ps(arr+[val])
                cal_num[idx] += 1

    ps()

    max_result = -100000000
    min_result = 100000000

    for part in cal_part:
        stack = list(reversed(numbers))
        i = 0
        
        while len(stack) != 1:
            a = stack.pop()
            b = stack.pop()

            if part[i] == '+':
                stack.append(a+b)
            
            elif part[i] == '-':
                stack.append(a-b)

            elif part[i] == '*':
                stack.append(a*b)
            
            elif part[i] == '/':
                stack.append(int(a/b))

            i += 1
  
        part_result = stack[0]

        if part_result >= max_result:
            max_result = part_result

        if part_result <= min_result:
            min_result = part_result

    print("#{0} {1}".format(t, max_result - min_result))