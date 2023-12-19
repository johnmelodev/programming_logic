# This program asks the user to input a maximum value and then prints all the numbers from 1 up to and including that maximum value.
# "for" is used to loop and keep the program going.
maximum_value = int(input('Enter the maximum value'))
initial_value = 1
for number in range(initial_value, maximum_value + 1):
    print(number)
