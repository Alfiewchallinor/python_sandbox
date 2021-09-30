import random
randomNumber = random.randint(1, 10)
print(randomNumber)
userGuess = int(input())

if randomNumber > userGuess:
    print("too low")
elif randomNumber < userGuess:
    print("too high")
else:
    print("correct")
