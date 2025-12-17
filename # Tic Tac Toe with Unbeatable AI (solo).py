# Tic Tac Toe with Unbeatable AI (Minimax Algorithm)

import math

def print_board(board):
    """Print the current board state."""
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_winner(board, player):
    """Check if a given player has won."""
    combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in combos)

def is_full(board):
    """Check if the board is full."""
    return all(space in ["X", "O"] for space in board)

def minimax(board, is_maximizing):
    """Minimax algorithm to evaluate best move."""
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:  # Computer's turn (O)
        best_score = -math.inf
        for i in range(9):
            if board[i] not in ["X", "O"]:
                board[i] = "O"
                score = minimax(board, False)
                board[i] = str(i+1)
                best_score = max(score, best_score)
        return best_score
    else:  # Player's turn (X)
        best_score = math.inf
        for i in range(9):
            if board[i] not in ["X", "O"]:
                board[i] = "X"
                score = minimax(board, True)
                board[i] = str(i+1)
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    """Find the best move for the computer using minimax."""
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] not in ["X", "O"]:
            board[i] = "O"
            score = minimax(board, False)
            board[i] = str(i+1)
            if score > best_score:
                best_score = score
                move = i
    return move

def tic_tac_toe():
    """Main game loop."""
    board = [str(i+1) for i in range(9)]
    print("Welcome to Tic Tac Toe!")
    print("You are X, Computer is O.")
    print("Choose a position by typing its number (1–9):")
    print_board(board)

    while True:
        # Player move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] in ["X", "O"]:
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue

        board[move] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("🎉 You win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        # Computer move
        comp_move = best_move(board)
        board[comp_move] = "O"
        print(f"Computer chose position {comp_move+1}")
        print_board(board)

        if check_winner(board, "O"):
            print("💻 Computer wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    tic_tac_toe()
