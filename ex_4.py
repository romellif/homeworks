"""
### Excercise 1.4 | Hotel fee (approx. 1,5 hours)
Write a program, where the user provides his age and the number of nights he wants to stay at the hotel.
Based on that values calculate the fee for his stay. The rules are:
- minor (below 18 years old) will pay 100 PLN per night
- adults (of age 18 but less than 65) will pay:
    - 200 PLN if they are staying for one night
    - 180 PLN if they are staying for at least 2 nights but less than 5
    - 150 PLN if they are staying for 5 and more nights
- pensioners (65 and older) will pay the same rate as adults but with a 10% discount
For example, if a user is 70 years old and will spend 10 nights at the hotel, he will pay 150 PLN - 10% discount = 135 PLN per night,
so for the whole stay, he will pay 1350 PLN.
"""

age = int(input('Enter your age: '))
nights = int(input('Enter the number of nights: '))

if age < 18:
    cost_per_night = 100

elif 18 <= age < 65:
    if nights == 1:
        cost_per_night = 200
    elif nights >= 5:
        cost_per_night= 150
    else:
        cost_per_night = 180

else:
    if nights == 1:
        cost_per_night = 200 * 90 / 100
    elif nights >= 5:
        cost_per_night = 150 * 90 / 100
    else:
        cost_per_night = 180 * 90 / 100

fee = cost_per_night * nights
print(f'The fee is {fee:.0f} PLN')