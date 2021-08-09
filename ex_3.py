"""
Write a program that will ask the user for his height (in cm) and body weight, and as a result will present his BMI and recommendations.
Take a look at BMI definition in wikipedia.
"""

height = int(input('Enter your height (cm): '))
weight = float(input('Enter your weight (Kg): '))

if height > 0 and weight > 0:

    bmi = weight/((height / 100) ** 2)
    print(f'Your BMI is {bmi:.1f} Kg/m2')
    if 0 < round(bmi, 1) < 18.5:
        print('Be careful. You are underweight!')
    elif 18.5 <= round(bmi, 1) <= 24.9:
        print('Nice result. You are normal weight!')
    elif 25 <= round(bmi, 1) <= 29.9:
        print('Watch out. You are overweight!')
    else:
        print('Attention. You might suffer from obesity!')

else:
    print('Something is wrong. Please re-enter your height and weight!')

