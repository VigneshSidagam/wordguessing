#WORD GUESSING GAME
import random
def fun():
    name = input("Enter your name:")
    print(f"Welcome to the word guessing game {name}")
    words = ('interpret peruse condone latent acrimonious indubitable propitious tremulous masquerade salient embroil languish aspersion sedulous pertinacious encumber effusion intrepid waffle mores disheveled sumptuous reciprocate infallible dissident dispatch intransigence pastoral concede manifold punitive salacious behoove vulpine premise demise megalomania asinine surfeit oblique jeopardize impudence ballast faze compunction caliber entreat antiquated anguish effeminate').split()
    computer = random.choice(words)
    total = []
    blank = ["_" for i in range(len(computer))]
    print(" ".join(blank))
    turns = 10
    while True:
        user = input("Enter your choice:")
        if len(user)==0:
            print("You have entered nothing, please enter something...!!!")
        else:
            if user in total:
                print("You already guessed this character, please enter another character...!!!")
            else:
                for i in range(len(computer)):
                    if user in computer[i]:
                        blank[i] = user
                print(" ".join(blank))
                total.append(user)
                if user not in computer:
                    print("Incorrect guess")
                    total.append(user)
                    turns -=1
                    print(f"You left with {turns} more turns")
                if "_" not in blank:
                    print("You guessed all the characters... You won the game...!!!")
                    break
                if turns == 0:
                    print("You lose the game...!!!")
                    print(f"The correct answer is {computer}")
                    break
fun()
ask = input("Do you wanna play again...?").lower()
while ask!="no":
    fun()
    ask = input("Do you wanna play again...?").lower()
else:
    print("Thankyou for playing word guessing game")
