"""
### Excercise 1.8 | Dog age calculator (approx. 0,5 hours)
Lets assume that 1 dog year equals 5 human years.
Ask a user what is the name of his dog and how old is he and calculate dogs age, if he would be a human.
Example:
Provide name of the dog - Lassie
Provide dogs age - 3
If Lassie was a human, would have 15 years.
"""

name = input('Provide name of the dog - ')
age_dog = int(input('Provide dogs age - '))

if age_dog >= 0:
    age_human = age_dog * 5
    print(f'If {name} was a human, would have {age_human} years.')
else:
    print('Please insert a valid age!')