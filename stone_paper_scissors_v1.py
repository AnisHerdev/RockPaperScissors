import random
ch=['Stone','Paper','Scissor']
def cls():
    print('\n'*70)
def show_points():
    print(f"{Player1} Points:",p1)
    print(f"{Player2} Points:",p2)

print("Hi there!!")
Num_players=input("1 player or 2 player?\n:")
Max_points=int(input("For how many points do you want to play?\n:"))

if Num_players == '1' or Num_players == '1 player' or Num_players == '1player':
    com=0
    Player1 = input("Player 1 name\n:").capitalize()
    for x in range (Max_points):
        computeri=random.choice(ch)
        Playeri=input( "Hey Stone or Paper or Scissor? \n:").capitalize()
        if Playeri == 'Stone'  and computeri == 'Scissor':
            print(f'{Player1} chose {Playeri} ,Computer chose {computeri}')
            print('You have got one point')
            p1=p1+1
        elif Playeri == 'Paper'  and computeri == 'Stone':
            print(f'{Player1} chose {Playeri} ,Computer chose {computeri}')
            print('You have got one point')
            p1=p1+1
        elif Playeri == 'Scissor'  and computeri == 'Paper':
            print(f'{Player1} chose {Playeri} ,Computer chose {computeri}')
            print('You have got one point')
            p1=p1+1
        elif Playeri == computeri:
           print(f'{Player1} chose {Playeri} ,Computer chose {computeri}')
           print('It is a tie both get a point!!')
        else:
            print(f'{Player1} chose {Playeri} ,Computer chose {computeri}')
            print("You did't get a point")
            com=com+1
        print()
    if p1>com:
        print('You win!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    elif p1==com:
       print("It is a tie.")
    else:
        print('You lose')

elif Num_players == '2' or Num_players == '2 player' or Num_players == '2player':
    p1=0
    p2=0
    Player1 = input("Player 1 name\n:").capitalize()
    Player2 = input("Player 2 name\n:").capitalize()
    for x in range (Max_points):
        p1i=input( f"Hey {Player1} Stone or Paper or Scissor? \n:").capitalize()
        cls()
        p2i=input( f"Hey {Player2} Stone or Paper or Scissor? \n:").capitalize()
        cls()
        if p1i == 'Stone' and p2i == 'Scissor':
            print('You have got one point',Player1)
            p1=p1+1

        elif p1i == 'Paper' and p2i == 'Stone':
            print('You have got one point',Player1)
            p1=p1+1

        elif  p1i == 'Scissor' and p2i == 'Paper':
            print('You have got one point',Player1)
            p1=p1+1

        elif p2i == 'Stone' and p1i == 'Scissor':
            print('You have got one point',Player2)
            p2=p2+1

        elif  p2i == 'Paper' and p1i == 'Stone':
            print('You have got one point',Player2)
            p2=p2+1

        elif  p2i == 'Scissor' and p1i == 'Paper':
            print('You have got one point',Player2)
            p2=p2+1

        elif p1i == p2i:
            print('Both got a point')
            p2=p2+1
            p1=p1+1

        else:
            print('no one got a point')

    print()
    if p1>p2:
        print('You win!!!!!!!!!!!!!',Player1,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        show_points()
    elif p1==p2:
        print("It is a tie.")
        show_points()
    else:
        print('You win!!!!!!!!!!!!!',Player2,'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        show_points()
