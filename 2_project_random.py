'''
5Q’s Method to set up an algorithm:
Critically analyze the problem and discover:
(Try to explain this problem to yourself out loud and ask for more information/investigate more until you fully understand the problem.)

1. What are the necessary input data?
- random value from 1 to 10
- user’s guess

2. What should I do with this data?
- I should compare the user’s guess with the random value that was generated at the beginning of the program and say if the guess was higher, lower, or equal to the value that was generated at the beginning of the program

3. What are the restrictions of this problem?
- A random value from 1 to 10

4. What is the expected result?
- The expected result is that the program should inform if the guess was above, below, or equal to the random value generated at the beginning of the program.

5. What is the sequence of steps to be taken to reach the expected result?
input random_value from 1 to 10
input guess
if guess > random_value
print “Guess was higher than the generated value”
if guess < random_value
print “Guess was lower than the generated value”
if guess = random_value
print “You got it right!”
'''

import random
random_value = random.randint(1, 10)
got_it_right = False
while got_it_right == False:
    guess = int(input('guess a value from 1 to 10'))
    if guess > random_value:
        print('Guess was higher than the generated value')
    elif guess < random_value:
        print('Guess was lower than the generated value')
    elif guess == random_value:
        got_it_right = True
        print('You got it right')
