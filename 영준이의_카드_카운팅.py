total_num = int(input())

for n in range(total_num):

    yung_card = list(input())
    y_c_list = []
    result = [13, 13, 13, 13]

    while yung_card:
        card = ''
        for i in range(3):
            card += yung_card[0]
            del yung_card[0]
        y_c_list.append(card)

    if len(set(y_c_list)) == len(y_c_list):
        for y_card in y_c_list:
            if y_card[0] == 'S':
                result[0] -= 1
            elif y_card[0] == 'D':
                result[1] -= 1
            elif y_card[0] == 'H':
                result[2] -= 1
            else:
                result[3] -= 1
        result = map(str, result)
        print('#{0} {1}'.format(n+1, ' '.join(result)))
    else:
        result = 'ERROR'
        print('#{0} {1}'.format(n+1, result))