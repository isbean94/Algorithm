def motion(X):
    global state

    if X == 'U':
        state = '^'
        field[state_idx[0]][state_idx[1]] = '^'
        if state_idx[0]-1 >= 0:
            if field[state_idx[0]-1][state_idx[1]] == '.':
                field[state_idx[0]-1][state_idx[1]] = state
                field[state_idx[0]][state_idx[1]] = '.'
                state_idx[0] -= 1

    if X == 'D':
        state = 'v'
        field[state_idx[0]][state_idx[1]] = 'v'
        if state_idx[0]+1 < H:
            if field[state_idx[0]+1][state_idx[1]] == '.':
                field[state_idx[0]+1][state_idx[1]] = state
                field[state_idx[0]][state_idx[1]] = '.'
                state_idx[0] += 1

    if X == 'L':
        state = '<'
        field[state_idx[0]][state_idx[1]] = '<'
        if state_idx[1]-1 >= 0:
            if field[state_idx[0]][state_idx[1]-1] == '.':
                field[state_idx[0]][state_idx[1]-1] = state
                field[state_idx[0]][state_idx[1]] = '.'
                state_idx[1] -= 1
            
    if X == 'R':
        state = '>'
        field[state_idx[0]][state_idx[1]] = '>'
        if state_idx[1]+1 < W:
            if field[state_idx[0]][state_idx[1]+1] == '.':
                field[state_idx[0]][state_idx[1]+1] = state
                field[state_idx[0]][state_idx[1]] = '.'
                state_idx[1] += 1

    if X == 'S':
        if state == '^':
            shoot = state_idx[0]
            while shoot >= 0:
                if field[shoot][state_idx[1]] == '#':
                    break
                elif field[shoot][state_idx[1]] == '*':
                    field[shoot][state_idx[1]] = '.'
                    break
                else:
                    shoot -= 1
        if state == 'v':
            shoot = state_idx[0]
            while shoot < H:
                if field[shoot][state_idx[1]] == '#':
                    break
                elif field[shoot][state_idx[1]] == '*':
                    field[shoot][state_idx[1]] = '.'
                    break
                else:
                    shoot += 1
        if state == '<':
            shoot = state_idx[1]
            while shoot >= 0:
                if field[state_idx[0]][shoot] == '#':
                    break
                elif field[state_idx[0]][shoot] == '*':
                    field[state_idx[0]][shoot] = '.'
                    break
                else:
                    shoot -= 1
        if state == '>':
            shoot = state_idx[1]
            while shoot < W:
                if field[state_idx[0]][shoot] == '#':
                    break
                elif field[state_idx[0]][shoot] == '*':
                    field[state_idx[0]][shoot] = '.'
                    break
                else:
                    shoot += 1

total_num = int(input())
for n in range(total_num):
    H, W = map(int, input().split())

    field = []
    for j in range(H):
        field.append([x for x in input()])
    for i in range(H):
        if '^' in field[i]:
            state = '^'
            state_idx = [i, field[i].index('^')]
        elif 'v' in field[i]:
            state = 'v'
            state_idx = [i, field[i].index('v')]
        elif '<' in field[i]:
            state = '<'
            state_idx = [i, field[i].index('<')]
        elif '>' in field[i]:
            state = '>'
            state_idx = [i, field[i].index('>')]
    
    N = int(input())
    motion_command = input()

    for X in motion_command:
        motion(X)

    print('#{0}'.format(n+1), end=" ")
    for k in range(H):
        print(''.join(field[k]))