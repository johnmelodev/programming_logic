# This code first prints ‘loading’ three times, then prints each name in the list: ‘jhonatan’, ‘cristian’, ‘roberto’, and ‘camila’. It uses for loops to iterate over a range and a list.
# it prints 3 times becaus the range starts in 0. so (1, 4) represents the space of 3 numbers if it was (0, 4). it would print 4 times
for word in range(1, 4):
    print('loading')

    names = ['jhonatan', 'cristian', 'roberto', 'camila']
    for name in names:
        print(name)
