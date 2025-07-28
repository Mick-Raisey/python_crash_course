# 9-14. Lottery: Make a list or tuple containing 15 numbers.
# Randomly select 4 numbers or letters from the list and print a message saying that
# any ticket matching these 4 numbers or letters wins a prize.

from random import choice

lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

winning_ticket = []
while len(winning_ticket) < 4:
    drawn_number = choice(lottery_numbers)

    if drawn_number not in winning_ticket:
        winning_ticket.append(drawn_number)

print(f"Winning Numbers: {winning_ticket}")
