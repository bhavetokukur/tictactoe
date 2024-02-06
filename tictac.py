table = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
player1 = 'x'
player2 = 'o'


def play(symbol):
    row = int(input('Chose the row '))
    column = int(input('Chose the column '))
    if table[row][column] != '-':
        raise Exception('Choose another position')

    table[row][column] = symbol
    # print(table)
    return


def seek_for_winner(symbol):
    # row checking
    for row in table:
        print(row)
        sum = 0
        for value in row:
            if value == symbol:
                sum += 1
        if sum == 3:
            return True
    # column checking
    for y in range(3):
        sum = 0
        for x in range(3):
            if table[x][y] == symbol:
                print("table[x][y]", x, y)
                sum += 1
        if sum == 3:
            return True
    # left-top to right-down diagonal checking
    sum = 0
    for y in range(3):
        if table[y][y] == symbol:
            sum += 1
        if sum == 3:
            return True
    # right-top to left-down checking
    sum = 0
    x = 2
    for y in range(3):
        if table[x][y] == symbol:
            sum += 1
        if sum == 3:
            return True
        x -= 1


def tie():
    count = 0
    for row in table:
        for value in row:
            if value != '-':
                count += 1
    if count == 9:
        return True


while True:
    play(player1)
    if seek_for_winner(player1):
        print('Player1 is a winner')
        exit()
    if tie():
        print('Game is tie')
        exit()

    play(player2)
    if seek_for_winner(player2):
        print('Player 2 is a winner')
        exit()

    if tie():
        print('Game is tie')
        exit()
