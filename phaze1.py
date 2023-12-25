##########Phase 1:
import random

#round number
i=1
points1=0
points2=0
player1= input("Enter player1 name:")
player2= input("Enter player2 name:")

def round (points1,points2):
    rand = random.randint(-5, 13)
    if(rand%2==0):
        points1 +=1
    else:
        points2 +=1
    return rand,points1,points2

def even_odd_game(i,points1,points2):
    i=1
    while points1 < 3 and points2 < 3:
        new_round,points1,points2 = round(points1,points2)
        winner = get_winner(points1, points2) 
        print_status(i, points1, points2, new_round, winner)
        if (points1==3 or points2==3):
            print(winner," Wins!")
            break
        i+=1

def print_status(i, points1, points2, new_round, winner):
    print("Round #",i , ", random number is",new_round , winner, "scored!" )
    print("Status: ",player1 ,points1,",",player2,points2)
    i+=1

def get_winner(points1, points2):
    if (points1 > points2):
        winner= player1
    else:
        winner= player2
    return winner
    
even_odd_game(i,points1,points2)



