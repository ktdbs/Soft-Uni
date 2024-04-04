num_of_letters = int(input())
sum_of_letters = 0
for _ in range(num_of_letters):
    letter = input()
    sum_of_letters+=ord(letter)

print(f'The sum equals: {sum_of_letters}')