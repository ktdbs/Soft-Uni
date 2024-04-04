import math

num_of_ppl = int(input())
elevator_capacity = int(input())
courses = math.ceil(num_of_ppl/elevator_capacity)
print(courses)