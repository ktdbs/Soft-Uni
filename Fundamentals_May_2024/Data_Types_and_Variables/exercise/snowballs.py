n = int(input())

snowball_weight = 0
snowball_time = 0
snowball_value = 0
snowball_quality = 0
for i in range(n):
    ball_weihgt = int(input())
    ball_time = int(input())
    quality = int(input())
    ball_value = int((ball_weihgt / ball_time) ** quality)
    if ball_value >snowball_value:
        snowball_value = ball_value
        snowball_weight = ball_weihgt
        snowball_time = ball_time
        snowball_quality = quality




print(f'{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})')