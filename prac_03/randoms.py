import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

#1  5 20
#2  3  9 , cannot produce 4
#3  2.5   <5.5

from random import randint
random_number = randint(1,100)
print(random_number)