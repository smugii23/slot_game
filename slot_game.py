"""
text-based slot machine
functionalities:
- user can deposit money
- allow user to bet on 1, 2, or 3 lines
- determine if they won
- allow them to keep playing if they won, or stop if they lose all their money.
"""
import random
MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {"777": 1, "A": 3, "B": 4, "C": 8}
symbol_values = {"777": 20, "A": 5, "B": 3, "C": 2}

def check_win(columns, lines, bet, values):
	winnings = 0
	winning_lines = []
	for line in range(lines):
		symbol = columns[0][line]
		for column in columns:
			symbol_check = column[line]
			if symbol != symbol_check:
				break
		else:
			winnings += values[symbol] * bet
			winning_lines.append(line + 1)
	return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
	all_symbols = []
	for symbol, symbol_count in symbols.items():
		for i in range(symbol_count):  # appends the symbol for how ever many occurences are in the symbol_count dictionary
			all_symbols.append(symbol)
			
	columns = []
	for col in range(cols):
		column = []
		current_symbols = all_symbols[:]
		for row in range(rows):
			value = random.choice(all_symbols)
			current_symbols.remove(value)  # so we do not pick it again
			column.append(value)
		columns.append(column)
	
	return columns

def print_slot_machine(columns):
	for row in range(len(columns[0])):
		for i, column in enumerate(columns):
			if i != len(columns) - 1:
				print(column[row], end = " | ")
			else:
				print(column[row], end = "")
		print()

def deposit():
	while True:
		amount = input("How much would you like to deposit? $")
		if amount.isdigit():
			amount = int(amount)
			if amount > 0:
				break
			else:
				print("Amount must be greater than 0.")
		else:
			print("Enter a valid number.")
			
	return amount

def number_of_lines():
	while True:
		lines = input("Enter the amount of lines to bet on (1-"+ str(MAX_LINES) + "):")
		if lines.isdigit():
			lines = int(lines)
			if 1 <= lines <= MAX_LINES:
				break
			else:
				print("Enter a valid number of lines.")
		else:
			print("Enter a valid number.")
			
	return lines	

def get_bet():
	while True:
		bet = input("Enter amount to bet: $")
		if bet.isdigit():
			bet = int(bet)
			if MIN_BET <= bet <= MAX_BET:
				break
			else:
				print(f"Enter a value between ${MIN_BET} and ${MAX_BET}.")
		else:
			print("Enter a valid number.")
			
	return bet		

def spin(balance):
	lines = number_of_lines()
	while True:
		bet = get_bet()
		total_bet = lines * bet
		if total_bet > balance:
			print(f"You do not have sufficient funds. Your balance is: {balance}")
		else:
			break
		
	print(f"You are betting ${bet} on {lines} lines. Total bet is: {total_bet}")
	slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
	print_slot_machine(slots)
	winnings, winning_lines = check_win(slots, lines, bet, symbol_values)
	print(f"You won ${winnings}.")
	print(f"You won on lines:", *winning_lines)
	return winnings - total_bet



def main():
	balance = deposit()
	while balance > 0:
		print(f"Current balance is: ${balance}")
		answer = input("Press enter to play, or q to quit.")
		if answer == "q":
			break
		balance += spin(balance)
	if balance == 0:
		print("You have run out of money.")
	
	print(f"You left with ${balance}.")

main()