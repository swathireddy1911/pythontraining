'''def greater(a,b,c):
    if (a>b) and (a>c):
        return("a is greater")
    elif b>a and b>c:
        return("b is greater")
    else:
        return("c is greater")
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
print(greater(a,b,c))


def year(a,b):
    if b==100:
        return("your age is 100 in 2021")
    else:
        age=100-b
        c=2021+age
        print("your age is ",b)
        return("your age will be 100 in the year %d "%c)
a=input("enter name")
b=int(input("enter age"))
print(year(a,b))'''




def game(player1,player2):
    while(player1 and player2)=="yes":
        player1=input("%s choose your option in the following :\n1.rock \n2.paper \n3.scissor" %p1)
        player2=input("%s choose your option in the following :\n1.rock \n2.paper \n3.scissor" %p2)
        if player1==player2:
            print("tie")
        elif player1=="rock":
            if player2=="scissor":
                print("%s congratu:ations you win" %p2)
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

p1=input("enter your name")
p2=input("enter your name")
print("you want to play the game?")
player1=input("%s enter your choice yes or no" %p1)
player2=input("%s enter your choice yes or no" %p2)
print(game(player1,player2))