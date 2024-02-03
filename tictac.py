table = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
player1 = 'x'
player2 = 'o'


def play(symbol):
    row = int(input('Chose the row'))
    column = int(input('Chose the column'))
    if table[row][column] != '-':
        raise Exception('Choose another position')

    table[row][column] = symbol
    # print(table)
    return


def seek_for_winner(symbol):
    for row in table:
        print(row)
        sum = 0
        for value in row:
            if value == symbol:
                sum += 1
        if sum == 3:
            return True

    for x in range(3):
        sum = 0
        for value in table:
            if value[x] == symbol:
                sum += 1
        if sum == 3:
            return True
            # print(column[x])


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
