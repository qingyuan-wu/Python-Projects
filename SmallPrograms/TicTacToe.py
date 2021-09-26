# Completed Oct 2020
# Tic Tac Toe game against the computer with AI improvements

import random

def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
    print("\n")

def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

# Part A
def num_to_coord(square_num):
    coord = []
    coord.append((square_num - 1) // 3)
    if square_num % 3 == 0:
        coord.append(2)
    if square_num % 3 == 2:
        coord.append(1)
    if square_num % 3 == 1:
        coord.append(0)

    return coord

# Part B
def put_in_board(board, mark, square_num):
    coord = num_to_coord(square_num)
    board[coord[0]][coord[1]] = mark
    print_board_and_legend(board)

# Part C
def user_input():
    mark = ""
    square_num = 0
    count = 0
    while count < 9:
        if count % 2 != 0:
            improve()
            if is_win(board, "O"):
                print_board_and_legend(board)
                print("The computer won.")
                return
            if improve2() == True:
                print_board_and_legend(board)
                count +=1
            else:
                make_random_move(board, "O")
                count +=1
        elif count % 2 == 0:
            move = input("Enter your move: ")
            square_num = int(move)
            put_in_board(board, "X", square_num)
            if count == 0 and square_num == 5:
                improve3()
                print_board_and_legend(board)
                count += 1

            if count == 0 and square_num != 5:
                improve4()
                print_board_and_legend(board)
                count += 1

            if is_win(board, "X"):
                print("Congratulations! You won!")
                return

            count += 1
        if count == 9:
            print("Tie.")

# Problem 2
# Part A
def get_free_squares(board):
    list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                list.append([i,j])

    return list

# Part B
def make_random_move(board, mark):
    possible_free_spaces = []
    possible_free_spaces = get_free_squares(board)
    random_position = int((len(possible_free_spaces) * random.random()))
    chosen_free_space = possible_free_spaces[random_position]
    board[chosen_free_space[0]][chosen_free_space[1]] = mark
    print_board_and_legend(board)


# Problem 3
def is_row_all_marks(board, row_i, mark):
    for i in board[row_i]:
        if i != mark:
            return False

    return True

def is_col_all_marks(board, col_i, mark):
    for i in range(3):
        if board[i][col_i] != mark:
            return False

    return True

def is_diag_all_marks(board, mark):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == mark:
        return True
    return False

def is_win(board, mark):
    for i in range(3):
        if is_row_all_marks(board, i, mark):
            return True
        if is_col_all_marks(board, i, mark):
            return True

    if is_diag_all_marks(board, mark):
        return True

    return False

def initialize():
    global board
    board = make_empty_board()
    print_board_and_legend(board)
    user_input()

def improve():
    free_spaces = get_free_squares(board)
    for i in free_spaces:
        board[i[0]][i[1]] = "O"
        if is_win(board, "O"):
            return
        else:
            board[i[0]][i[1]] = " "


def improve2():
    free_spaces = get_free_squares(board)
    for i in free_spaces:
        board[i[0]][i[1]] = "X"
        if is_win(board, "X"):
            board[i[0]][i[1]] = "O"
            return True
        else:
            board[i[0]][i[1]] = " "

    return False


def improve3():
    board[0][0] = "O"

def improve4():
    board[1][1] = "O"

if __name__ == '__main__':
    initialize()