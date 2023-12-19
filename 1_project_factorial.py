'''
EXAMPLE: Factorial of a number

Create a program that receives a number and prints its factorial.

5Q’s Method to set up an algorithm:

Critically analyze the problem and discover:
(Try to explain this problem to yourself out loud and ask for more information/investigate more until you fully understand
the problem.)

1. What are the necessary input data?
number

2. What should I do with this data?
I should calculate the factorial of the number that is passed to my program and display it on the screen

3. What are the restrictions of this problem?
- the number must have a positive value
- the number must be an integer

4. What is the expected result?
- The expected result is that the factorial of the provided number is displayed.

5. What is the sequence of steps to be taken to reach the expected result?
input number
if number > 0
if number = integer
factorial = 1
loop from 1 to number
factorial = factorial * number
'''

number = int(input('type number'))
if number > 0:
    factorial = 1
    for item in range(1, number + 1):
        factorial = factorial * item
    print(factorial)
