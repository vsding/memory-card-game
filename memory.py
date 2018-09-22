import random, sys, time

# Constants
HIDDEN_CARD = '#'
QUIT = 'q'
HINT = 'h'
MIN_DIMENSION = 2
MAX_DIMENSION = 10

# Global var to keep track of whether game has been won
game_won = False

def choose_card(current_board, answer_board, dim):
	print("\nType the row index and column index--separated by a space--of the card you want to flip")
	row = None
	col = None
	while row not in range(1, dim+1) or col not in range(1, dim+1):
		print("Enter integers between 1 and " + str(dim) + ":")
		print("(Or type q to quit or h for a hint)")
		input_str = raw_input()
		if input_str == QUIT:
			quit_game(answer_board, dim)
			return -1 # indicates quit
		if input_str == HINT:
			get_hint(current_board, answer_board, dim) 
		try:
			row, col = map(int, input_str.split())
		except:
			pass
	return (row-1, col-1)


def check_cards_match(card1, card2, current_board, answer_board):
	x1, y1 = card1
	x2, y2 = card2
	if answer_board[x1][y1] == answer_board[x2][y2]:
		print("\nIt\'s a match! :)\n")
		current_board[x1][y1] = answer_board[x1][y1]
		current_board[x2][y2] = answer_board[x2][y2]
	else:
		print("Not a match - try again!\n")


def get_hint(current_board, answer_board, dim):
	hidden_cards = []
	for row in range(dim):
		for col in range(dim):
			if current_board[row][col] == HIDDEN_CARD:
				hidden_cards.append( (row, col) )
	reveal_row, reveal_col = random.choice(hidden_cards)
	print("\nHint: The character " + str(answer_board[reveal_row][reveal_col]) + \
		" appears at row " + str(reveal_row+1) + ", column " + str(reveal_col+1) + ".\n")


def quit_game(answer_board, dim):
	print("\nThe board was:\n")
	for row in range(dim):
		for col in range(dim):
			print(answer_board[row][col]), 
		print('\n')
	print("Good-bye!\n")


def flip_cards(current_board, answer_board, dim):	
	card1 = choose_card(current_board, answer_board, dim)
	if card1 == -1: # quit
		return False
	display_board(current_board, answer_board, dim, card1)

	card2 = choose_card(current_board, answer_board, dim)
	if card2 == -1: # quit
		return False
	display_board(current_board, answer_board, dim, card1, card2)

	check_cards_match(card1, card2, current_board, answer_board)

	if any(HIDDEN_CARD in row for row in current_board): # cards remaining, keep playing
		return True
	else:
		global game_won
		game_won = True


def display_board(current_board, answer_board, dim, *squares):
	print('\n')
	for row in range(dim):
		for col in range(dim):
			if (row, col) in squares:
				print(answer_board[row][col]), 
			else:
				print(current_board[row][col]),
		print('\n')

def print_intro_rules():
	print("\n\n=================")
	print("WELCOME TO MEMORY")
	print("=================\n")
	print("RULES:\n")
	print("- Whenever prompted, type the row index and column index--separated by a space--of the card you want to reveal")
	print("- Rows and columns are 1-indexed")
	print("  For example: 1 1 (upper leftmost card)")
	print("               4 4 (bottom rightmost card)") 
	print("- At any point in the game, enter q to quit or h for a hint ;)")


def init_board(dim):
	card_vals = []
	for i in range(65, 65 + (dim*dim) / 2):
		card_vals.append(chr(i))
		card_vals.append(chr(i))

	random.shuffle(card_vals)
	answer_board = []
	for i in range(dim):
		answer_board.append(list(card_vals[dim * i : dim * (i+1)]))
	current_board = [list(HIDDEN_CARD * dim) for i in range(dim)]

	return current_board, answer_board


def prompt_dimension():
	print("\n\nBEFORE WE BEGIN... choose how large you want the board to be.")
	print("\nThe game board is an n by n square.")
	dimension = 0

	while dimension < MIN_DIMENSION or dimension > MAX_DIMENSION or dimension % 2 != 0:
		print("Enter an even number n between " + str(MIN_DIMENSION) + " and " \
			+ str(MAX_DIMENSION) + ", inclusive:")
		dimension = raw_input()
		try:
			dimension = int(dimension)
		except:
			pass
	return dimension


def main():
	print_intro_rules()
	dimension = prompt_dimension()
	current_board, answer_board = init_board(dimension)
	num_turns = 0
	start_time = time.time()
	display_board(current_board, answer_board, dimension)

	while flip_cards(current_board, answer_board, dimension):
		num_turns += 1

	global game_won
	if game_won:
		print("Congrats - you've completed the game!")
		print("It took you " + str(num_turns+1) + " turns and " + \
			str(round(time.time() - start_time)) + " seconds to match all the pairs.\n")


if __name__ == '__main__':
	main()