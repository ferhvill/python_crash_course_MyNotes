car = ["one", "two", "three"]
for names in car:
    print(f"{names.title()}, that's nice")
    print(f"I can't wait to see again {names.title()}")

for value in range(6):
    print(value)

even = list(range(2, 11, 2))
print(even)

for value in range(1, 11):
    square = value**2
    print(square)

square = []
for value in range(1, 11):
    square.append(value**2)
print(square)

squares = [value**2 for value in range(1, 11)]
print(squares)

scal = [a for a in range(5)]
print(scal)

mill = list(range(1000000))
print(mill)

players = ["ana", "flor", "juan", "mike", "jon"]
for name in players[1:4]:
    print(name)

pla2 = players[:]
print(pla2)
players.append("fer")
print(players)
