alien = {"color": "green", "points": 5}
print(alien)
alien["x"] = 5
alien["y"] = 10
print(alien)

# WE USE DEL FOR REMOVE A PAIR IN A DICTIONARY
del alien["y"]
print(alien)

# GET METHOD WHEN WE ARE NOT SURE ABOUT A KEY
print(alien.get("y", "Doesn't exist"))

# LOOPING A DICTIONARY
for key, value in alien.items():
    print(f"The key {key} contains the value {value}")

for k, v in alien.items():
    print(f"Key: {k}")
    print(f"Value: {v}")
######################################################

fav_language = {
    "juan": "c",
    "pedro": "python",
    "ana": "java",
    "santi": "rust",
    "angel": "c",
    "fidel": "c",
}

friends = ["juan", "lucas"]

for name in fav_language.keys():
    print(f"Hi {name.title()}!")

    if name in friends:
        language = fav_language.get(name, "None").title()
        print(f"\t Hey {name.title()}, I see you love {language}")

for name in sorted(fav_language.keys()):
    print(f"Hey {name.title()}, thank you for participating")

for language in fav_language.values():
    print(f"{language.title()}")

for language in set(
    fav_language.values()
):  # the SET method just takes the unique values
    print(f"{language.title()}")

my_set = {"c", "python", "c", "javascript", "rust"}
print(my_set)


###### NESTING DICTIONARIES

# We create an empty list
aliens = []

# Make 30 aliens
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "high"
        alien["points"] = 15

for alien in aliens[0:5]:
    print(alien)

print(f"Total number of aliens: {len(aliens)}")


#########################################################################
# A list in a dictionary
fav_languages = {
    "juan": ["c"],
    "pedro": ["python", "ruby"],
    "ana": ["java"],
    "fer": ["c", "python", "java"],
}

for name, languages in fav_languages.items():
    print(f"The favorite languages of {name.title()} are:")
    for language in languages:
        print(f"\t{language.title()}")

#########################################################################
# A dictionary in a dictionary

users = {
    "eurbina": {
        "first": "eliana",
        "last": "urbina",
        "age": 27,
    },
    "fhinojosa": {
        "first": "fernando",
        "last": "hinojosa",
        "age": 31,
    },
    "dperez": {
        "first": "daniel",
        "last": "perez",
        "age": 15,
    },
}

for username, user_info in users.items():
    print(f"Username: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    age = f"{user_info['age']}"

    print(f"\tFull name: {full_name.title()}")
    print(f"\tAge: {age}")
