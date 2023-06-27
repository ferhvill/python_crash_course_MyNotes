############################################################################################
# ______   ___   ___   ________   ______   _________  ______   ______        _______       #
# /_____/\ /__/\ /__/\ /_______/\ /_____/\ /________/\/_____/\ /_____/\      /______/\      #
# \:::__\/ \::\ \\  \ \\::: _  \ \\:::_ \ \\__.::.__\/\::::_\/_\:::_ \ \     \__::::\ \     #
# \:\ \  __\::\/_\ .\ \\::(_)  \ \\:(_) \ \  \::\ \   \:\/___/\\:(_) ) )_        \::\ \    #
#  \:\ \/_/\\:: ___::\ \\:: __  \ \\: ___\/   \::\ \   \::___\/_\: __ `\ \        \::\ \   #
#   \:\_\ \ \\: \ \\::\ \\:.\ \  \ \\ \ \      \::\ \   \:\____/\\ \ `\ \ \        \: \ \  #
#    \_____\/ \__\/ \::\/ \__\/\__\/ \_\/       \__\/    \_____\/ \_\/ \_\/         \:_\/  #
#                                                                                          #
############################################################################################

################################    I  N   P   U   T   S    ################################
# Clear Prompts
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

# Accepting int values
age = input("How old are you? ")
age = int(age)
age >= 18

# Another example
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou are not allowed to enter!")

# Even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")


################################    WHILE LOOPS    ################################
number = 1
while number <= 5:
    print(number)
    number += 1
