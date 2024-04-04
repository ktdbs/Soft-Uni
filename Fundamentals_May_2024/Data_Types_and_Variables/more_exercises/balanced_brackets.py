num_of_lines = int(input())
current_string = ''
is_unbalanced = False
open_bracket = False
closing_bracket_count = 0
open_bracket_count = 0
current_bracket = ''
for line in range(num_of_lines):
    random_string = input()
    if random_string == '(':
        if current_bracket == random_string:
            is_unbalanced = True
        current_bracket = '('
        open_bracket_count +=1
    elif random_string == ')':
        if current_bracket == '(':
            is_unbalanced = False
            current_bracket = ''
        else:
            is_unbalanced = True
        closing_bracket_count +=1

if is_unbalanced or closing_bracket_count != open_bracket_count:
    print('UNBALANCED')
else:
    print('BALANCED')



