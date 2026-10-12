
# Tic-Tac-Toe with Simple AI
# CodeOrbit Tech - Artificial Intelligence Internship

HUMAN = "X"
COMPUTER = "O"
EMPTY = " "


def display_board(board):
    """Display the game board."""
    for row in range(3):
        print(" " + " | ".join(board[row * 3:row * 3 + 3]))
        if row < 2:
            print("---+---+---")
    print()


def check_winner(board, player):
    """Check if a player has won."""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def is_draw(board):
    """Check if all positions are filled."""
    return EMPTY not in board


def minimax(board, is_maximizing):
    """Find the best move using the Minimax algorithm."""

    if check_winner(board, COMPUTER):
        return 1

    if check_winner(board, HUMAN):
        return -1

    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = COMPUTER
                score = minimax(board, False)
                board[i] = EMPTY
                best_score = max(best_score, score)

        return best_score

    best_score = float("inf")

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = HUMAN
            score = minimax(board, True)
            board[i] = EMPTY
            best_score = min(best_score, score)

    return best_score


def computer_move(board):
    """Choose the best available move."""
    best_score = float("-inf")
    best_move = None

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = COMPUTER
            score = minimax(board, False)
            board[i] = EMPTY

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def play_game():
    """Play Tic-Tac-Toe against the computer."""
    board = [EMPTY] * 9

    print("Welcome to Tic-Tac-Toe!")
    print("You are X. The computer is O.")
    print("Choose positions from 1 to 9.")

    while True:
        # Display position numbers for empty cells.
        numbered_board = [
            str(i + 1) if board[i] == EMPTY else board[i]
            for i in range(9)
        ]
        display_board(numbered_board)

        # Get the human player's move.
        try:
            position = int(input("Enter your position (1-9): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if position < 1 or position > 9:
            print("Choose a position between 1 and 9.")
            continue

        if board[position - 1] != EMPTY:
            print("That position is already occupied!")
            continue

        board[position - 1] = HUMAN

        if check_winner(board, HUMAN):
            display_board(board)
            print("Congratulations! You win!")
            break

        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # Let the computer make its move.
        move = computer_move(board)
        board[move] = COMPUTER
        print("Computer chose position:", move + 1)

        if check_winner(board, COMPUTER):
            display_board(board)
            print("The computer wins! Better luck next time.")
            break

        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
