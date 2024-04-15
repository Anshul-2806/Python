import random

while True:
    print("1. stone 2. paper 3. scissor")
    user_input = int(input("Enter the Number "))

while user_input > 3 or user_input < 1:
        print("Enter valid choice number between 1 to 3")

if user_input == 1:
    user_input_choice = 'Stone'
elif user_input == 2:
    user_input_choice = 'Paper'
else:
    user_input_choice = 'Scissor'

print("user has selected", user_input_choice)
device_choice = random.randint(1,3)

while user_input == device_choice:
    device_choice = random.randint(1, 3)

if device_input == 1:
    device_input_choice = 'Stone'
elif device_input == 2:
    device_input_choice = 'Paper'
else:
    device_input_choice = 'Scissor'

print("Device has selected",device_input_choice)

if (user_input == 1 and device_choice == 2) or (user_input == 2 and device_choice == 1):
    print("Stone wins in this situation")
    result = 'Stone'

elif (user_input == 1 and device_choice == 2) or (user_input == 2 and device_choice == 1):
    print("Paper wins in this situation")
    result = 'Paper'

else:
    print("Scissor wins in this situation")
    result = 'Scissor'


if user_input_choice == result:
    print("User wins the Game")
else:
    print("Device wins the Game")

print("Wou;d you like to play again  ?")
print("Y for Yes & N for No")
rematch = input()
if rematch == 'n' or rematch == 'N':
    print("Thanks for play....")