import random 

x = random.randint(1,6)
y = random.random()

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

cards = [1, 2, 3, 4, 5, "A", "B", "C"]

random.shuffle(cards)

print(x)
print(y)
print(z)
print(cards)