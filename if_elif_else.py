# Conditionals
# if, elife else

# I arrived late for class, can I still enter? If this is not your third time being late, then yes, otherwise you will be suspended.


number_of_delays = int(input('type number'))
if number_of_delays >= 3:
    print('You are suspended')
elif number_of_delays == 1:
    print('You can enter, but if you have 2 more delays, you will be suspended')
elif number_of_delays == 2:
    print('You can enter, but if you have 1 more delay, you will be suspended')
else:
    print('You can enter')
