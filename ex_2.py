"""
### Excercise 1.2 | Shoemaker (approx. 1 hours)
Ask the user to provide a number of days of the week (Monday=1, Sunday=7) when he left his shoes at the shoemaker shop for a repair.
Ask him also how many days the repair will take. As an output, inform the user at which day of the week he should get back his shoes.
For example, leaving shoes on Tuesday with 3 days needed for the repair, should output Friday
"""

day_of_the_week = int(input('Provide day of the week (Monday=1, Sunday=7): '))
repair_days = int(input('How many days will the repair take? '))
giveback = day_of_the_week + repair_days

if 1 <= day_of_the_week <= 7 and repair_days >= 0:

    if giveback == 1:
        print('Your shoes will be ready on Monday')

    elif giveback == 2:
        print('Your shoes will be ready on Tuesday')

    elif giveback == 3:
        print('Your shoes will be ready on Wednesday')

    elif giveback == 4:
        print('Your shoes will be ready on Thursday')

    elif giveback == 5:
        print('Your shoes will be ready on Friday')

    elif giveback == 6:
        print('Your shoes will be ready on Saturday')

    elif giveback == 7:
        print('Your shoes will be ready on Sunday')

    elif giveback == 8:
        print('Your shoes will be ready next week on Monday')

    elif giveback == 9:
        print('Your shoes will be ready next week on Tuesday')

    elif giveback == 10:
        print('Your shoes will be ready next week on Wednesday')

    elif giveback == 11:
        print('Your shoes will be ready next week on Thursday')

    elif giveback == 12:
        print('Your shoes will be ready next week on Friday')

    elif giveback == 13:
        print('Your shoes will be ready next week on Saturday')

    elif giveback == 14:
        print('Your shoes will be ready next week on Sunday')

    else:
        x = int((giveback - (giveback % 7)) / 7)
        y = giveback % 7

        if y == 1:
            print(f'Your shoes will be ready in {x} weeks on Monday')

        elif y == 2:
            print(f'Your shoes will be ready in {x} weeks on Tuesday')

        elif y == 3:
            print(f'Your shoes will be ready in {x} weeks on Wednesday')

        elif y == 4:
            print(f'Your shoes will be ready in {x} weeks on Thursday')

        elif y == 5:
            print(f'Your shoes will be ready in {x} weeks on Friday')

        elif y == 6:
            print(f'Your shoes will be ready in {x} weeks on Saturday')

        else:
            print(f'Your shoes will be ready in {x - 1} weeks on Sunday')

else:
    print('You entered a wrong input: please insert a valid day/reparation time!')