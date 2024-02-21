print("Welcom to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() !="Yes".lower():
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does  CPU stand for? \n Ans: ")

if answer.lower() == "central processing unit".lower():
    print("Correct!")
    score+=1.5
else:
    print("Incorrect!")


answer = input("What does GPU stand for? \n Ans: ")

if answer.lower() == "graphics processing unit".lower():
    print("Correct!")
    score+=1.5
else:
    print("Incorrect!")

answer = input("What does RAM stand for? \n Ans: ")

if answer.lower() == "random access memory".lower():
    print("Correct!")
    score+=1.5
else:
    print("Incorrect!")

answer = input("What does PSU stand for? \n Ans: ")

if answer.lower() == "power supply unit".lower():
    print("Correct!")
    score+=1.5
else:
    print("Incorrect!")

print("You got "+ str(score) +" number worth questions correct!")

print ("You got "+str((score / 6) * 100) + "%.")

