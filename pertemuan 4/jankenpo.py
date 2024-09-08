player1 = input("(player 1) batu, gunting, kertas? = ")
player2 = input("(player 2) batu, gunting, kertas? = ")

player1 = player1.lower()
player2 = player2.lower()

if (player1 == "gunting" and player2 == "batu"):
    print()
    print("Player 2 Win")
elif (player1 =="gunting" and player2 == "kertas"):
    print()
    print("Player 1 Win")
elif (player1 =="gunting" and player2 == "gunting"):
    print()
    print("Draw")
elif (player1 =="kertas" and player2 == "batu"):
    print()
    print("Player 1 Win")
elif (player1 =="kertas" and player2 == "gunting"):
    print()
    print("Player 2 Win")
elif (player1 =="kertas" and player2 == "kertas"):
    print()
    print("Draw")
elif (player1 =="batu" and player2 == "kertas"):
    print()
    print("Player 2 Win")
elif (player1 =="batu" and player2 == "gunting"):
    print()
    print("Player 1 Win")
elif (player1 =="batu" and player2 == "batu"):
    print()
    print("draw")
else :
    print()
    print("salah satu atau kedua pilihan gerakan player tidak sesuai")