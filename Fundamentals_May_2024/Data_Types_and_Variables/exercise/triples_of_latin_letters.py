
num_of_letters = int(input())

for i1 in range(0,num_of_letters):
    for i2 in range(0,num_of_letters):
        for i3 in range(0,num_of_letters):
            print(f'{chr(97 +i1)}{chr(97+i2)}{chr(97+i3)}')

