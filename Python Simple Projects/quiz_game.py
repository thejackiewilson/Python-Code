print("Welcome to the NBA Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Hoop! Please type in letters, no numbers!")
score = 0

answer = input ("How tall is CP3? ")
if answer.lower() == "six foot":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input ("How tall is Kyle Lowry? ")
if answer.lower() == "six foot":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input ("How tall is Davion Mitchell? ")
if answer.lower() == "six foot":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input ("How tall is Trey Burke? ")
if answer.lower() == "six foot":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input ("How tall is Mo Bamba? ")
if answer.lower() == "seven foot":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input ("What is the length of an NBA court in feet? ")
if answer.lower() == "ninety four feet":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " +str(score) + " questions correct!")
print("You got " +str((score / 6) * 100) + "%!")

    