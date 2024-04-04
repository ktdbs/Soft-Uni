import math

num = int(input())
is_prime = True

devider = int(math.sqrt(num))
for i in range (2, devider +1):
    if num % i == 0:
        is_prime = False

print(is_prime)