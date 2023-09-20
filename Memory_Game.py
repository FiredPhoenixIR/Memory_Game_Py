import random

def initialize_board(size):
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_pairs = size * size // 2
    pairs = random.sample(symbols, num_pairs)
    board = pairs + pairs
    random.shuffle(board)
    return [board[i:i+size] for i in range(0, len(board), size)]

def display_board(board, revealed):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if revealed[i][j]:
                print(board[i][j], end=' ')
            else:
                print('?', end=' ')
        print()

def is_game_over(revealed):
    for row in revealed:
        if False in row:
            return False
    return True

def main():
    size = 4  # Adjust this for different board sizes (e.g., 4x4, 6x6, etc.)
    board = initialize_board(size)
    revealed = [[False] * size for _ in range(size)]
    moves = 0

    while not is_game_over(revealed):
        print("\n--- Memory Game ---")
        display_board(board, revealed)
        print("\nEnter row and column to reveal a card (e.g., '1 2'): ")
        
        try:
            row, col = map(int, input().split())
            if 1 <= row <= size and 1 <= col <= size and not revealed[row-1][col-1]:
                revealed[row-1][col-1] = True
            else:
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Enter row and column as integers.")
            continue

        if moves % 2 == 1:
            if board[row-1][col-1] != board[prev_row-1][prev_col-1]:
                revealed[row-1][col-1] = False
                revealed[prev_row-1][prev_col-1] = False
        else:
            prev_row, prev_col = row, col

        moves += 1

    print("Congratulations! You won in", moves, "moves.")

if __name__ == "__main__":
    main()
