secret = 27
attempts = 0
lives = 5
print("Number guessing game")
print("Guess the number between 1 and 50")
while attempts < 5:
    guess=int(input("Enter Your Guess: "))
    attempts = attempts+1
    if guess == secret:
        print("You win!")
        break
    else:
        difference = abs(secret - guess)
        if difference > 20:
            print("ice cold")
        elif difference > 10:
            print("Cold")
        elif difference > 5:
            print("Warm")
        else:
            print("hot")
        lives = lives - 1
        print("Lives left:", end="")
        for i in range(lives):
            print("lives", end="")
if guess != secret:
    print("you lost")
    print("the secret number was ", secret)
        
