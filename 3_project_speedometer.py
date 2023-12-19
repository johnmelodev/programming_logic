'''
Project - Speedometer

Considering the maximum speed limit of 80km on a certain street. Create a
program that receives from the user a value that represents the speed and based on this speed
say if they got a light, serious or very serious fine. Considering that if the person
is below the maximum speed your program should display “no fine”, if it is up to
10km above, it should display: “got a light fine”, if it is between 11 to 20km above the speed
maximum, display: “got a serious fine”, and if it is above 20km above the maximum speed,
display: “got a very serious fine”.

Critically analyze the problem and discover: (Try to explain this problem to yourself out loud and ask for more
information/investigate more until you fully understand the problem.)

1. What are the necessary input data?
- speed

2. What should I do with this data?
- Considering that if the person
is below the maximum speed your program should display “no fine”, if it is up to
10km above, it should display: “got a light fine”, if it is between 11 to 20km above the speed
maximum, display: “got a serious fine”, and if it is above 20km above the maximum speed,
display: “got a very serious fine”

3. What are the restrictions of this problem?

4. What is the expected result?
- The expected result is to display the message that corresponds to the level of the fine that the person got
(should display: “got a light fine”, if it is between 11 to 20km above the maximum speed,
display: “got a serious fine”, and if it is above 20km from the maximum speed, display: "got
a very serious fine"

5. What is the sequence of steps to be taken to reach the expected result?
input speed
maximum_speed = 80
if speed <= maximum_speed:
print “No fine”
if speed > maximum_speed and speed <= maximum_speed + 10:
print “Got a light fine”
if speed > maximum_speed +11 and speed <= maximum_speed + 20:
print “Got a serious fine”
if speed > maximum_speed + 20:
print “Got a very serious fine”
'''

speed = int(input('Enter your speed'))
maximum_speed = 80
if speed <= maximum_speed:
    print('No fine')
elif speed > maximum_speed and speed <= maximum_speed + 10:
    print('Got a light fine')
elif speed >= maximum_speed + 11 and speed <= maximum_speed + 20:
    print('Got a serious fine')
elif speed >= maximum_speed + 20:
    print('Got a very serious fine')
