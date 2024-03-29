import math

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (3 * len(row) - 1))

# Function to check if the current player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == player for row in range(len(board))):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(len(board))) or all(board[i][len(board)-1-i] == player for i in range(len(board))):
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Function to evaluate the board for the current player
def evaluate_board(board, player):
    if check_winner(board, player):
        return 1
    elif check_winner(board, "X" if player == "O" else "O"):
        return -1
    else:
        return 0

# Minimax algorithm function
def minimax(board, depth, is_maximizing_player):
    # Base case: If the game is over or depth limit is reached, evaluate the board
    if is_board_full(board) or check_winner(board, "X") or check_winner(board, "O") or depth == 0:
        return evaluate_board(board, "O")

    if is_maximizing_player:
        max_eval = -math.inf
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth - 1, False)
                    max_eval = max(max_eval, eval)
                    board[i][j] = " "
        return max_eval
    else:
        min_eval = math.inf
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth - 1, True)
                    min_eval = min(min_eval, eval)
                    board[i][j] = " "
        return min_eval

# Function to find the best move for the current player using Minimax algorithm
def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                board[i][j] = "O"
                eval = minimax(board, 4, False)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Main function to play the game
def main():
    board = [[" "]*3 for _ in range(3)]
    print("Welcome to Tic Tac Toe!")

    while not is_board_full(board) and not check_winner(board, "X") and not check_winner(board, "O"):
        print_board(board)

        # Player X's turn
        row = int(input("Player X, enter row number (0, 1, 2): "))
        col = int(input("Player X, enter column number (0, 1, 2): "))
        while board[row][col] != " ":
            print("That cell is already occupied. Try again.")
            row = int(input("Player X, enter row number (0, 1, 2): "))
            col = int(input("Player X, enter column number (0, 1, 2): "))
        board[row][col] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("Player X wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Player O's turn (AI)
        print("Player O is thinking...")
        row, col = find_best_move(board)
        board[row][col] = "O"

        if check_winner(board, "O"):
            print_board(board)
            print("Player O wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
