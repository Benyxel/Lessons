print("Hello Welcome to my Game")

Playing = input ("Do you wanna play? ")

if Playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0

answer = input("What is the capital town of Ghana? ")
if answer.lower() == "accra":
    print(" Bravo!, you are right")
    score += 1
    
else:
    print("Oops, Incorrect")

#Question 2
answer = input("What is the name given to a monday born child in Ghana? ")
if answer.lower() == "kwadwo":
    print(" Bravo!, keep going")
    score += 1
else:
    print("Oops, Incorrect")

#Question 3
answer = input("What is the Common Language in Ghana? ")
if answer.lower() == "twi":
    print(" Bravo!, you are the best")
    score += 1
else:
    print("Oops, Incorrect")   

print("You got " + str(score) + " quetions correct!")