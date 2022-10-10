import random

def hangman ():
    word =random.choice (["pokemon","avengers","confident","great","consistent","beautiful","selfdependent","intern","religious"])
    validletter = 'abcdefghijklmnopqrstuvwxyz'
    turns=10
    guessmade=''

    while len(word)>0:
        main=""
        missed = 0
        
        for letter in word:
            if letter in guessmade:
                main=main+letter
            else:
                main=main+"_"+""
        if main==word:
            print(main)
            print("wow🥰🥰!! you have saved him")
            break

        print("Guess the word: ", main)
        guess=input()

        if guess in validletter:
            guessmade=guessmade+guess
        else:
            print("enter a valid letter")
            guess=input()
        
        if guess not in word:
            turns=turns-1

            if turns == 9:
                print("9 turns left")
                print("___________")
            if turns == 8:
                print("8 turns left")
                print("___________")
                print("     0     ")
            if turns == 7:
                print("7 turns left")
                print("___________")
                print("     0     ")
                print("     |     ")
            if turns==6:
                print("6 turns left")
                print("___________")
                print("     0     ")
                print("     |     ")
                print("    /      ")
            if turns == 5:
                print("5 turns left")
                print("___________")
                print("     0     ")
                print("     |     ")
                print("    / \    ")
            if turns == 4:
                print("4 turns left")
                print("___________")
                print("   \ 0     ")
                print("     |     ")
                print("    / \    ")
            if turns == 3:
                print("3 turns left")
                print("___________")
                print("   \ 0 /   ")
                print("     |     ")
                print("    / \    ")
            if turns == 2:
                print("2 turns left")
                print("___________")
                print("   \ 0 /|  ")
                print("     |     ")
                print("    / \    ")
            if turns == 1:
                print("1 turns left")
                print("last breaths counting, take care")
                print("___________")
                print("   \ 0_|/  ")
                print("     |     ")
                print("    / \    ")
            if turns == 0:
                print("😞😞 You let a kind man die")
                print("___________")
                print("     0_|  ")
                print("    /|\     ")
                print("    / \    ")
                break

name = input("enter the name sir/mam ")
print("welcome" , name)
print("________________")
print("try to guess the word in 10 attempts")
hangman()
print()