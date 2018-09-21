import random, sys

# Constants
DIM = 2# Dim must be even... eventually ask user input
HIDDEN_CARD = '#'
QUIT = 'q'
HINT = 'h'

card_vals = []
for i in range(65, 65 + (DIM*DIM) / 2):
	card_vals.append(chr(i))
	card_vals.append(chr(i))

random.shuffle(card_vals)
answer_board = []
for i in range(DIM):
	answer_board.append(list(card_vals[DIM * i : DIM * (i+1)]))
current_board = [list(HIDDEN_CARD * DIM) for i in range(DIM)]
game_won = False

def display_board(*squares):
	print('\n')
	for row in range(DIM):
		for col in range(DIM):
			if (row, col) in squares:
				print(answer_board[row][col]), 
			else:
				print(current_board[row][col]),
		print('\n')


def choose_card():
	print("\nType the row index and column index--separated by a space--of the card you want to flip")
	row = None
	col = None
	while row not in range(1, DIM+1) or col not in range(1, DIM+1):
		print("Enter integers between 1 and " + str(DIM) + ":")
		print("(Or type q to quit or h for a hint)")
		input_str = raw_input()
		if input_str == QUIT:
			quit_game()
			return -1 
		if input_str == HINT:
			get_hint() 
		try:
			row, col = map(int, input_str.split())
		except:
			pass
	return (row-1, col-1)

def check_cards_match(card1, card2):
	x1, y1 = card1
	x2, y2 = card2
	if answer_board[x1][y1] == answer_board[x2][y2]:
		print("\nIt\'s a match! :)\n")
		current_board[x1][y1] = answer_board[x1][y1]
		current_board[x2][y2] = answer_board[x2][y2]
	else:
		print("Not a match - try again!\n")


def get_hint():
	hidden_cards = []
	for row in range(DIM):
		for col in range(DIM):
			if current_board[row][col] == HIDDEN_CARD:
				hidden_cards.append( (row, col) )
	reveal_row, reveal_col = random.choice(hidden_cards)
	print("\nHint: The letter " + str(answer_board[reveal_row][reveal_col]) + \
		" appears at row " + str(reveal_row+1) + ", column " + str(reveal_col+1) + ".\n")


def quit_game():
	print("\nThe board was:\n")
	for row in range(DIM):
		for col in range(DIM):
			print(answer_board[row][col]), 
		print('\n')
	print("Good-bye!\n")


def flip_cards():	
	card1 = choose_card()
	if card1 == -1: # quit
		return False
	display_board(card1)

	card2 = choose_card()
	if card2 == -1: # quit
		return False
	display_board(card1, card2)

	check_cards_match(card1, card2)

	if any(HIDDEN_CARD in row for row in current_board): # cards remaining, keep playing
		return True
	else:
		global game_won
		game_won = True


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


def main():
	num_turns = 0
	print_intro_rules()
	display_board()
	while flip_cards():
		num_turns += 1
		pass
	global game_won
	if game_won:
		print("Congrats - you've completed the game!")
		print("It took you " + str(num_turns+1) + " turns to match all the pairs.\n")

if __name__ == '__main__':
	main()