import random
#How to import random number (randrange/randint)
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please input a number larger than 0")
        quit()

else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
print(random_number )

while True:
    user_quess = input("Make a quess: ")
    if user_quess.isdigit():
       user_quess = int(user_quess)

    else: 
       print("Please type a number next time.")
       continue 

    if user_quess == random_number:
        print("You go it!")
        break
    else:
        print("You got it wrong")
