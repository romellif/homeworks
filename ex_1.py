"""
## 1. Interaction with the user
### Excercise 1.1 | Interaction with the user and simple calculations (approx. 2 hours)
Ask user (using `input()` function) to provide the number of kilograms of potatoes he'd like to buy and how much 1-kilogram costs.
The program should display how much user have to pay."""

kg = float(input('Kg of potatoes: '))
cost_per_kg = float(input('Cost per kg: '))

cost = kg * cost_per_kg
print(f'For {kg:.2f} Kg of potatoes you have to pay {cost:.2f} $')