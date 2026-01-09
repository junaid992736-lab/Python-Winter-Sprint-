#ROCK PAPER SCISSOR GAME
import random
print("ROCK PAPER SCISSOR GAME")
User_move=input("Enter Your Move (Rock/Paper/Scissor):")
Moves=("Rock","Paper","Scissor")
Computer_move=random.choice(Moves)


print("\nOpponent's Move Is ",Computer_move )
print("     RESULT     ")


if User_move==Computer_move:
    print("    Draw    ")
elif User_move=="Rock"and Computer_move=="Scissor":
    print("    You win    ")
elif User_move=="Paper"and Computer_move=="Rock":
    print("    You win    ")
elif User_move=="Scissor"and Computer_move=="Paper":
    print("    You win    ")
else:
    print("    You Lose    ")
print("     THANKYOU     ")