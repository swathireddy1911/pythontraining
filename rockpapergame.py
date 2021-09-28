p1=input("enter your name")
p2=input("enter your name")
print("you want to play the game?")
player1=input("%s enter your choice yes or no" %p1)
player2=input("%s enter your choice yes or no" %p2)
while(player1 and player2)=="yes":
    player1=input("%s choose your option in the following :\n1.rock \n2.paper \n3.scissor" %p1)
    player2=input("%s choose your option in the following :\n1.rock \n2.paper \n3.scissor" %p2)
    if player1==player2:
        print("tie")
    elif player1=="rock":
        if player2=="scissor":
            print("%s congratulations you win" %p2)
        else:
            print("%s congratulations you win" %p1)
    elif player1=="paper":
        if player2=="scissor":
            print("%s congratulations you win" %p2)
        else:
            print("%s congratulations you win" %p1)
    elif player1=="scissor":
        if player2=="rock":
            print("%s congratulations you win" %p2)
        else:
            print("%s congratulations you win" %p1)
    else:
        print("invalid game")
    print("you want to contuniue the game?")
    player1=input("%s enter your choice yes or no" %p1)
    player2=input("%s enter your choice yes or no" %p2)

