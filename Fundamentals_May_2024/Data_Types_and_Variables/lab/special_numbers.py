num = int(input())

# V1
for number in range(1, num +1):
    num_to_string = str(number)
    digit_sum = 0
    is_special_num = False
    for digit in num_to_string:
        digit_sum += int(digit)
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        is_special_num = True
    print(f'{num_to_string} -> {is_special_num}')

# V2
# for number in range(1, num + 1):
#     sum_of_digits = 0
#     is_special = False
#     current_num = number
#     while current_num > 0:
#         digit = current_num % 10
#         sum_of_digits += digit
#         current_num = int(current_num / 10)
#     if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
#         is_special = True
#     print(f'{number} -> {is_special}')
