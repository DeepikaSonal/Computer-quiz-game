from tkinter.messagebox import YES


print ("Welcome to Computer Quiz Program !")

playing = input ("hey! Hi, Do you want to play? " )

if playing.lower() != "yes":
    quit()

print("OK ! let's play :)") 
score = 0  

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")  

answer = input("Who is the father of Computer science? ")
if answer.lower() == "charles babbage":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

answer = input("What converts an entire program into machine language? ")
if answer.lower() == "compiler":
    print("Correct!")
    score += 1
else:
    print("Incorrect!") 

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")  

print("you got "+ str(score) + " questions correct !")       
print("you got "+ str((score / 4)*100) + "%")            