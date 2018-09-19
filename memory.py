import random, sys

DIM = 4 # Dim must be even... eventually ask user input
HIDDEN_CARD = 'x'

cards = list('1122334455667788')
random.shuffle(cards)
answer_board = [cards[:4], cards[4:8], cards[8:12], cards[12:]]
current_board = [list(HIDDEN_CARD * 4) for i in range(DIM)]
# num_turns = 0

def display_board(*cards):
	print('\n')
	for row in range(len(answer_board)):
		for col in range(len(answer_board[0])):
			if (row, col) in cards:
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
		# print("[Type q to quit or h for a hint]")
		try:
			row, col = map(int, raw_input().split())
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


def flip_cards():	
	card1 = choose_card()
	display_board(card1)
	card2 = choose_card()
	display_board(card1, card2)
	check_cards_match(card1, card2)

	if any(HIDDEN_CARD in row for row in current_board): # cards remaining, keep playing
		return True


def print_intro_rules():
	print("\n\nWELCOME TO MEMORY")
	print("Rules:")
	print("- Whenever prompted, type the row index and column index--separated by a space--of the card you want to reveal")
	print("- Rows and columns are 1-indexed")
	print("  For example: 1 1 (upper leftmost card)")
	print("			4 4 (bottom rightmost card)") 
	# print("At any point in the game, type q to quit or h for a hint ;)")


def main():
	print_intro_rules()
	display_board()
	while flip_cards():
		pass
	print("Congrats!")
	# print("It took you " + str(num_turns) + " to match all the pairs.")

if __name__ == '__main__':
	main()