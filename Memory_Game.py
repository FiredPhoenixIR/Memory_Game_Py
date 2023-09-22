import random
import time

def generate_cards(num_pairs):
    icons = ["A", "B", "C", "D", "E", "F", "G", "H"]
    cards = icons * num_pairs
    random.shuffle(cards)
    return cards

def display_board(board):
    for row in board:
        print(" ".join(row))

def main():
    num_pairs = 4  # Number of pairs of cards
    cards = generate_cards(num_pairs)
    board_size = (4, num_pairs * 2)
    board = [["#" for _ in range(board_size[1])] for _ in range(board_size[0])]
    
    matched_pairs = 0
    moves = 0
    start_time = time.time()

    while matched_pairs < num_pairs:
        display_board(board)
        print(f"Moves: {moves}")
        print(f"Time Elapsed: {int(time.time() - start_time)} seconds\n")
        
        try:
            choice1 = tuple(map(int, input("Enter the row and column of the first card (e.g., 1 2): ").split()))
            choice2 = tuple(map(int, input("Enter the row and column of the second card (e.g., 2 3): ").split()))
        except ValueError:
            print("Invalid input. Please enter row and column as integers.")
            continue
        
        if (
            choice1 != choice2 and
            0 <= choice1[0] < board_size[0] and 0 <= choice1[1] < board_size[1] and
            0 <= choice2[0] < board_size[0] and 0 <= choice2[1] < board_size[1]
        ):
            card1 = board[choice1[0]][choice1[1]]
            card2 = board[choice2[0]][choice2[1]]
            
            if card1 == card2 and card1 != "#":
                print("Match!")
                board[choice1[0]][choice1[1]] = card1
                board[choice2[0]][choice2[1]] = card2
                matched_pairs += 1
            else:
                print("No match. Try again.")
            
            moves += 1
        else:
            print("Invalid choice. Please choose valid cards.")
    
    end_time = time.time()
    elapsed_time = int(end_time - start_time)
    print(f"Congratulations! You completed the game in {moves} moves and {elapsed_time} seconds.")

if __name__ == "__main__":
    main()
