import random

bankacc = 100
bet = 0


while bankacc != 0:
    
    handchoice = raw_input("Please choose R(Rock), P(Paper), or S(Scissors): ")
    handchoice = handchoice.upper()
    if(handchoice == 'EXIT' or handchoice.startswith('E') or handchoice == 'QUIT' or handchoice.startswith('q')):
        break
    compchoice = random.randint(1,3)
    betchoice = int(raw_input("Please place a bet: "))

    if(betchoice > bankacc):
        print("You need to bet a smaller amount next time")
        break
    if(compchoice == 1):
        compchoice = "Rock"
    if(compchoice == 2):
        compchoice = "Paper"
    if(compchoice == 3):
        compchoice = "Scissors"


    print("The computer chose: " + compchoice)
    print("You chose: " + handchoice)

    if(handchoice == "R" and compchoice == "Scissors"):
        print("You win!")
        bankacc += betchoice
    if(handchoice == "R" and compchoice == "Rock"):
        print("It's a tie.")
    if(handchoice == "R" and compchoice == "Paper"):
        print("You lost...")
        bankacc = bankacc - betchoice

    if(handchoice == "P" and compchoice == "Rock"):
        print("You win!")
        bankacc += betchoice
    if(handchoice == "P" and compchoice == "Paper"):
        print("It's a tie.")
    if(handchoice == "P" and compchoice == "Scissors"):
        print("You lost...")
        bankacc = bankacc - betchoice

    if(handchoice == "S" and compchoice == "Paper"):
        print("You win!")
        bankacc += betchoice
    if(handchoice == "S" and compchoice == "Scissors"):
        print("It's a tie.")
    if(handchoice == "S" and compchoice == "Rock"):
        print("You lost...")
        bankacc = bankacc - betchoice

    elif(handchoice != "R"):
        print("Please enter a valid input")
    elif(handchoice != "S"):
        print("Please enter a valid input")
    elif(handchoice != "P"):
        print("Please enter a valid input")
        print(" ")

    if(bankacc != 0):
        print("You currently have ") + str(bankacc)
    else:
        print("You lost all your money!")
