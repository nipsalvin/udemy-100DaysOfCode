def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(str(cell) if cell != ' ' else str(i * 3 + j + 1) for j, cell in enumerate(row)))
        if i < 2:
            print("-" * 10)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if 1 <= move <= 9:
                # divmod() is a built-in Python function that takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder when divided
                return divmod(move - 1, 3)
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row, col = get_player_move(current_player)

        if board[row][col] == ' ':
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            # Switch to the other player
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()

