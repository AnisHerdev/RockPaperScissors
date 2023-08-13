import random

def cls(): #To skip 70 lines so that player 2 can't see what player 1 entered
    print('\n'*70)
def show_points(p1,p2): #To diaplay the points of the players
    print(f"{p1['name']} Points: {p1['points']}")
    print(f"{p2['name']} Points: {p2['points']}")
def check_winner(p1,p2): #To check who won
    if p1['points']>p2['points']:
        print(f'{p1["name"]} wins!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        show_points(p1,p2)
    elif p1['points']==p2['points']:
        print("It is a tie.")
        show_points(p1,p2)
    else:
        print(f'{p2["name"]} wins!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        show_points(p1,p2)

print("Hi there!!")
while True:
    Num_players=input("1 player or 2 player?\n:")
    if Num_players in ('1','1 player','1player','one','2','2 player','2player','two'):
        break
    print('Try using 1 or 2 for (1 player or 2 player).')
Max_points=int(input("For how many points do you want to play?\n:"))
ch=['Stone','Paper','Scissor']

if Num_players in ('1','1 player','1player','one'):
    computer={'name':'Computer','points':0}
    Player1 = {'name':input("Player 1 name?\n:").capitalize(),'points':0}
    for x in range (Max_points):
        computeri=random.choice(ch) #To randomly choose stone paper or scissors
        Playeri=input(f"Hey {Player1['name']} Stone or Paper or Scissor? \n:").capitalize()
        if Playeri == 'Stone'  and computeri == 'Scissor':
            print(f'{Player1["name"]} chose {Playeri} ,Computer chose {computeri}')
            print(f'You have got one point,{Player1["name"]}')
            Player1['points']+=1
        elif Playeri == 'Paper'  and computeri == 'Stone':
            print(f'{Player1["name"]} chose {Playeri} ,Computer chose {computeri}')
            print(f'You have got one point,{Player1["name"]}')
            Player1['points']+=1
        elif Playeri == 'Scissor'  and computeri == 'Paper':
            print(f'{Player1["name"]} chose {Playeri} ,Computer chose {computeri}')
            print(f'You have got one point,{Player1["name"]}')
            Player1['points']+=1
        elif Playeri == computeri:
            print(f'{Player1["name"]} chose {Playeri} ,Computer chose {computeri}')
            print('It is a tie both get a point!!')
            Player1['points']+=1
            computer['points']+=1
        elif Playeri not in ch:
            print('no one got a point')
        else:
            print(f'{Player1["name"]} chose {Playeri} ,Computer chose {computeri}')
            print(f"You did't get a point,{Player1['name']}")
            computer['points']+=1
        print()
    check_winner(Player1,computer)
    
elif Num_players in  ('2','2 player','2player','two'):
    p2=0
    Player1 = {'name':input("Player 1 name?\n:").capitalize(),'points':0}
    Player2 = {'name':input("Player 2 name?\n:").capitalize(),'points':0}
    for x in range (Max_points):
        p1i=input( f"Hey {Player1['name']} Stone or Paper or Scissor? \n:").capitalize()
        cls()
        p2i=input( f"Hey {Player2['name']} Stone or Paper or Scissor? \n:").capitalize()
        cls()
        if p1i == 'Stone' and p2i == 'Scissor':
            print('You have got one point',Player1['name'])
            Player1['points']+=1
        elif p1i == 'Paper' and p2i == 'Stone':
            print('You have got one point',Player1['name'])
            Player1['points']+=1
        elif  p1i == 'Scissor' and p2i == 'Paper':
            print('You have got one point',Player1['name'])
            Player1['points']+=1
        elif p1i == p2i:
            print('Both got a point')
            Player2['points']+=1
            Player1['points']+=1
        elif p1i not in ch or p2i not in ch:
            print('no one got a point')
        else:
            print('You have got one point',Player2['name'])
            Player2['points']+=1           
    print()
    check_winner(Player1,Player2)


