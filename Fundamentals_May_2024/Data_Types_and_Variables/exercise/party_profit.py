import math

group_size = int(input())
days = int(input())
companions_count = group_size
coins = 0
cost = 0

for day in range (1, days +1):
    if day % 10 == 0:
        companions_count -=2
    if day % 15 == 0:
        companions_count +=5
    coins += 50
    cost += 2 * companions_count
    if day % 3 == 0:
        cost += 3 *companions_count
    if day % 5 == 0:
        coins += 20 * companions_count
        if day % 3 == 0 :
            cost += 2 * companions_count

coins_per_companion = math.floor((coins-cost)/companions_count)

print(f'{companions_count} companions received {coins_per_companion} coins each.')