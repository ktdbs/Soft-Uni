year = int(input())

#V1
# while True:
#     year+=1
#     year_to_string = str(year)
#     next_happy_year = ''
#     for digit in year_to_string:
#         if digit in next_happy_year:
#             break
#         next_happy_year += digit
#     if len(year_to_string) == len(next_happy_year):
#         print(next_happy_year)
#         break


#V2
while True:
    year+=1
    year_to_string = str(year)
    year_to_set = set(year_to_string)
    if len(year_to_string)== len(year_to_set):
        print(year)
        break





