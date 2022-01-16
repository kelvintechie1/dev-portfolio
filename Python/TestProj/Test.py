# Test PyCharm
import time

people = ['Trevor', 'Meow']

print("In 5 seconds, I'm going to say that the following people suck: " + str(people))
time.sleep(5)

for peoples in people:
    print(peoples + " sucks!")

i = 0

while i < 5:
    print(".")
    i += 1

print("Furthermore, " + people[0] + ", your opinion is irrelevant. You suck.")

print("Ha, I win!")