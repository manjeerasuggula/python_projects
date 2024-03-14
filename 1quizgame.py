print("welcome to my computer quiz!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("what does the CPU stands for? ").lower()
if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does the GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does the RAM stands for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does the PSU stands for? ")
if answer.lower() == "power supply":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " Questions correct!")
print("your got " + str((score / 4) * 100) + "%.")
