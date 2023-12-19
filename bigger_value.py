'''
This Python script demonstrates a basic comparison operation. It prompts the user to enter two values.
Then, the script compares these two values and prints on the screen which one is larger.
'''

First_value = input('Enter the 1st value:')
Second_value = input('Enter the 2nd value')

if int(First_value) > int(Second_value):
    print('First value is bigger!')
else:
    print('Second value is bigger!')
