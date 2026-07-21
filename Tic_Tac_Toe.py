import random

BOARD_SIZE = 3
PLAYER, COMPUTER = "X", "O"


def print_board(board):
    print("\nBoard:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def available_moves(board):
    return [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] == " "]


def check_winner(board):
    lines = []

    for i in range(BOARD_SIZE):
        lines.append(board[i])
        lines.append([board[r][i] for r in range(BOARD_SIZE)])

    lines.append([board[i][i] for i in range(BOARD_SIZE)])
    lines.append([board[i][BOARD_SIZE - 1 - i] for i in range(BOARD_SIZE)])

    for line in lines:
        if line.count(line[0]) == BOARD_SIZE and line[0] != " ":
            return line[0]

    if not available_moves(board):
        return "Tie"
    return None


def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == COMPUTER:
        return 10 - depth
    if winner == PLAYER:
        return depth - 10
    if winner == "Tie":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for (r, c) in available_moves(board):
            board[r][c] = COMPUTER
            score = minimax(board, depth + 1, False)
            board[r][c] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for (r, c) in available_moves(board):
            board[r][c] = PLAYER
            score = minimax(board, depth + 1, True)
            board[r][c] = " "
            best_score = min(best_score, score)
        return best_score


def computer_move(board):
    best_score = -float("inf")
    best_move = None
    for (r, c) in available_moves(board):
        board[r][c] = COMPUTER
        score = minimax(board, 0, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            best_move = (r, c)
    return best_move


def player_move(board):
    while True:
        try:
            user_input = input("Enter your move as row,col (1-3,1-3): ")
            row, col = [int(x.strip()) - 1 for x in user_input.split(",")]
            if (row, col) in available_moves(board):
                return row, col
            print("That cell is already taken or invalid. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter values like 1,3.")


def main():
    print("Welcome to Tic Tac Toe!")
    print("You are X, computer is O.")
    board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_player = PLAYER if random.choice([True, False]) else COMPUTER

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break

        if current_player == PLAYER:
            row, col = player_move(board)
            board[row][col] = PLAYER
            current_player = COMPUTER
        else:
            print("Computer is thinking...")
            row, col = computer_move(board)
            board[row][col] = COMPUTER
            current_player = PLAYER

    print_board(board)


if __name__ == "__main__":
    main()
