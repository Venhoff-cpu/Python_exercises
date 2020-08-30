# initial sudoku board/grid
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def find_empty(board):
    """
    Searches the board for "0" - an empty space
    :param board: partially complete board
    :return: returns a tuple with empty row, col - (row: int, col: int)
    """

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j

    return None


def valid(board, pos, num):
    """
    Returns if the attempted move is valid
    :param board: 2d list - board of sudoku
    :param pos: position on board for param num - tuple (row, col)
    :param num: number to be verified in specified pos
    :return: bool
    """

    # row validation
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Column validation
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[1] != i:
            return False

    # In box validation
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(board):
    """
    Util - prints solved sudoku board
    :param board: 2d List of ints - solved sudoku board
    :return: None
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j == 8:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="")


def solve(board):
    """
    function for solving sudoku board using backtracking
    :param board: 2d list of ints - initial sudoku board with empty spaces
    :return: solved sudoku board or False if no correct solution
    """
    empty_pos = find_empty(board)
    if empty_pos:
        for i in range(1, 10):
            if valid(board, empty_pos, i):
                board[empty_pos[0]][empty_pos[1]] = i

                if solve(board):
                    return True

                board[empty_pos[0]][empty_pos[1]] = 0
    else:
        return True

    return False


if __name__ == "__main__":
    if solve(grid):
        print_board(grid)
    else:
        print('No possible solution for provided board')
