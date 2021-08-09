"""
Write a program that, based on the player's position (x, y) on the board in the range from 0 to 100,
displays its approximate location (center, upper right corner, upper edge, ...)
or information about the position outside the board. Take the value 10 as an edge margin.

Sample program output:
Enter player's X position: 95
Enter player's Y position: 95
The player is in the upper right corner.
"""

x = int(input("Enter player's X position: "))
y = int(input("Enter player's Y position: "))

if 0 <= x <= 10:
    if 0 <= y <= 10:
        print('The player is in the bottom left corner')
    elif 10 < y < 90:
        print('The player is on the left side')
    elif 90 <= y <= 100:
        print('The player is in the upper left corner')
    else:
        print('The player is outside the board')

elif 10 < x < 90:
    if 0 <= y <= 10:
        print('The player is on the bottom side')
    elif 10 < y < 90:
        print('The player is in the center')
    elif 90 <= y <= 100:
        print('The player is on the top side')
    else:
        print('The player is outside the board')

elif 90 <= x <= 100:
    if 0 <= y <= 10:
        print('The player is in the bottom right corner')
    elif 10 < y < 90:
        print('The player is on the right side')
    elif 90 <= y <= 100:
        print('The player is in the upper right corner')
    else:
        print('The player is outside the board')

else:
    print('The player is outside the board')