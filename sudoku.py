import pickle

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

test = [
    [3, 8, 0, 4, 0, 0, 0, 2, 1],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(bo):
    for i in range(len(bo)):
        if i == 0:
            print(" @ - - - - - - - - - - - - @")
        if i % 3 == 0 and i != 0:
            print(" | - - - - - - - - - - - - |")

        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j], "| ")
            else:
                print(str(bo[i][j]) + " ", end="")
    print(" @ - - - - - - - - - - - - @")


def choose_cell(bo):
    while True:
        radidx = input("Row: ")
        if radidx == 'menu':
            return 0
        colidx = int(input("Col: "))
        radidx = int(radidx)
        if (0 < radidx < 10) and (0 < colidx < 10):
            break
        else:
            print("Not in range")
    ny_value = int(input("Value: "))
    if ny_value == '-':
        bo[radidx - 1][colidx - 1] = 0
    else:
        for x in range(0, 8):
            if (ny_value == (bo[radidx-1][x])) or (ny_value == (bo[x][colidx-1])):
                print("Not valid:/")
                return choose_cell(bo)
        bo[radidx - 1][colidx - 1] = ny_value
    return bo


def save_game(brett):
    f = open('save_game.txt', 'w')  # w spesifiserer at filen skal skrives til
    f.write(brett)
    f.close()
    return brett


def open_game(brett):
    f = open(brett, 'r')  # r spesifiserer at man skal lese fra en fil
    innhold = f.read()
    f.close()
    return innhold


def lagre(brett, filnavn):
    with open(filnavn, 'wb') as fp:
        pickle.dump(brett, fp)


def opne(brett):
    with open(brett, 'rb') as fp:
        bo = pickle.load(fp)
        return bo


def main(game):
    while True:
        print_board(game)
        while True:
            i = choose_cell(game)
            if i == 0:
                break
            print_board(game)
        hva = input(": ")
        if hva == 'save':
            filnavn = input('Filnavn: ')
            lagre(game, filnavn)
            print("Saved as: ", filnavn)
            main(game)
        if hva == "open":
            brett = input('filnavn:')
            main(opne(brett))


lagre(test, 'testfil.exe')
main(board)
