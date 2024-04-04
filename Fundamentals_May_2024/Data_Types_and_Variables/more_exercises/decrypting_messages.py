decrypted_message = ''
key_int = int(input())
num_of_chars = int(input())
for _ in range(num_of_chars):
    char_input = input()
    new_ch = chr(ord(char_input) + key_int)
    decrypted_message += new_ch

print(decrypted_message)