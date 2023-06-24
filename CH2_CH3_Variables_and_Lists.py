# firstname = "ada "
# secondname = "lovelace"
# full = f"{firstname} {secondname}"
# print(f"Hello, {full.title()}!")
# print(firstname)

# CLEANING INPUT STRINGS
# firstname.rstrip() or firstname.lstrip()

################## LISTS #######################
moto = ["honda", "ducati", "suzuki"]
moto.append("kawa")
moto.insert(1, "kawa")  # INSERT allow us put a new value in the desired position
print(moto)
# del moto[1] # delete an element from list
second = moto.pop(1)  # POP is to remove a value but using the removed value
print(second)
print(moto)
too_expensive = "ducati"
moto.remove(
    too_expensive
)  # REMOVE allows us to remove by the name of the value (similar to pop()). We need to run a for loop to delete repeated values
print(moto)
print(f"\nA {too_expensive.title()} is too expensive")
moto.sort()
print(moto)
print(len(moto))
