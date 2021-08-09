"""
### Excercise 1.6 | Tickets (approx. 1 hour)
Assumptions:
    - 0-6   - kindergarten - ticket price: 0
    - 7-17  - school       - ticket price: 2.28
    - 18-64 - adult        - ticket price: 3.80
    - +65   - pensioner    - ticket price: 1.90
Write a program that will ask a user for his age and a number of tickets he'd like to buy.
Based on the assumptions above calculate the price he should pay for the tickets.
"""

age = int(input('Enter your age: '))
tickets = int(input('Enter the number of tickets: '))

if tickets > 0:
    if age <= 6:
        cost = 0
        print('Free ticket for you!')
    else:
        if age >= 7 and age <= 17:
            cost = 2.28
        elif age >= 18 and age <= 64:
            cost = 3.80
        else:
            cost = 1.90
        price = tickets * cost
        print(f'The total amount you have to pay is {price} $')
else:
    print("You didn't buy any ticket")

