ans = input("Enter the answer to the riddle")
riddle= input ("enter your riddle")
guess = ""
guess_count = 0
print(riddle)
while guess.lower()!= ans.lower() and guess_count<3:
    guess = input("Enter your answer")
    guess_count+=1
if guess.lower() == ans.lower() :
    print("You win ")
else:
    print("you are out of guesses")
