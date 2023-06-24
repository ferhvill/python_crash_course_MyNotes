list = ["uno", "dos", "tres", "cuatro"]
a = "one" in list
print(a)

banned_user = ["juan", "pedro", "ana", "felipe"]
user = "jon"

if user not in banned_user:
    print(f" Hey {user.upper()} you cannot write here")

alien_color = input("Enter a color: ")

if alien_color == "green":
    print("You earned 5 points")
elif alien_color == "yellow":
    print("You earned 10 points")
else:
    print("You earned 15 points")

list1 = [1, 2, 3]
if list1:
    print("tengo elementos")
else:
    print("estoy vacia")

available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "pineapple",
    "extra cheese",
]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"{topping} was added to your pizza")
    else:
        print(f"Sorry, {topping} is not currently available")
print("Your order was received")
#####################################################################################################
usernames = ["admin", "fer99", "ana123", "juan99", "susan2"]

if usernames:
    for user in usernames:
        if user == "admin":
            print(f"Hello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again")
else:
    print("We need to find some users")

#####################################################################################################

current_users = ["Admin", "Fer99", "ana123", "Juan99", "Susan2"]
new_users = ["sara2", "fer991", "holy1", "Rafa2", "Ana123"]

current_users_lw = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lw:
        print(f"{user} already exist. Try another username")
    else:
        print(f"The user name {user} is available")

#####################################################################################################
