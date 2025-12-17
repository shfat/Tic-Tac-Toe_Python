from termcolor import colored
from colorama import init

init()

winner = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)
moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))


def print_board(board):
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n\n"
        if i == "X":
            print(colored(f"[{i}]", "red"), end=end)
        elif i == "O":
            print(colored(f"[{i}]", "blue"), end=end)
        else:
            print(f"[{i}]", end=end)
        j += 1


def can_move(brd, mve):
    return mve in range(1, 10) and isinstance(brd[mve - 1], int)


def is_winner(brd, plyr):
    for tup in winner:
        if all(brd[j] == plyr for j in tup):
            return True
    return False


def make_move(brd, plyr, mve, undo=False):
    if can_move(brd, mve):
        brd[mve - 1] = plyr
        win = is_winner(brd, plyr)
        if undo:
            brd[mve - 1] = mve
        return True, win
    return False, False


def has_empty_space(board):
    return board.count("X") + board.count("O") != 9


def computer_move(board, player, computer):
    mv = -1
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break
    if mv == -1:
        for j in range(1, 10):
            if make_move(board, player, j, True)[1]:
                mv = j
                break
    if mv == -1:
        for tup in moves:
            for m in tup:
                if mv == -1 and can_move(board, m):
                    mv = m
                    break
    return make_move(board, computer, mv)


def play_game():
    board = list(range(1, 10))
    player, computer = "X", "O"
    winner_found = False

    print("player: X \ncomputer: O\n")

    while has_empty_space(board):
        print_board(board)
        try:
            move = int(input("choose a move: "))
        except ValueError:
            print("Please enter a number between 1-9.")
            continue

        moved, won = make_move(board, player, move)
        if not moved:
            print("invalid number, please try again")
            continue
        if won:
            print(colored("you won!", "green"))
            winner_found = True
            break
        elif computer_move(board, player, computer)[1]:
            print(colored("you lost!", "yellow"))
            winner_found = True
            break

    print_board(board)
    if not winner_found:
        print(colored("It's a draw!", "cyan"))


# === منوی اصلی ===
while True:
    print("\n1. Start Game")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        play_game()
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
