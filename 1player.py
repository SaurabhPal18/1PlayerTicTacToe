import os 
import sys
import random
game=[" "," "," "," "," "," "," "," "," "]
def print_game():
    os.system('cls') #clear the screen
    print(game[0]+" |"+game[1]+" |"+game[2])
    print("__|__|__")
    print(game[3]+" |"+game[4]+" |"+game[5])
    print("__|__|__")
    print(game[6]+" |"+game[7]+" |"+game[8])
def begin():
    n=2
    print("1.For x 2.For y")
    tr=int(input())
    if tr==1:
        player1='x'
        player2='o'
    else:
        player1='o'
        player2='x'
    while True:
        print("Player 1 turn")
        player(player1)
        n=check_result(player1,player2)
        draw(game)
        if n==1:
            sys.exit()
        print("Player 2 turn")
        player_computer(player1,player2)
        n=check_result(player1,player2)
        draw(game)
        if n==1:
            sys.exit()
def player(p):
    print("Tell the place you want to enter")
    t=int(input())
    if game[t-1] !=" ":
           print("Not empty")
           player(p)
    else:
        game[t-1]=p  #here game is a list
        print_game()
def check_result(p1,p2):
    value=6
    for i in range(8):
        if game[i]==" ":
            game[i]=6
    solution1=list(set((game[0],game[1],game[2])))
    solution2=list(set((game[0],game[3],game[6])))
    solution3=list(set((game[0],game[4],game[8])))
    solution4=list(set((game[1],game[4],game[7])))
    solution5=list(set((game[2],game[5],game[8])))
    solution6=list(set((game[3],game[4],game[5])))
    solution7=list(set((game[6],game[7],game[8])))
    solution8=list(set((game[2],game[4],game[6])))
    result=[solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8]
    global q
    q=5
    for i in range(8):
        if len(result[i])==1 and result[i][0] !=6:
            q=1
            if result[i][0]== p1:
                print("Player 1 wins ")
            else:
                print("Player  2 wins")
            value=5
        
       
    for i in range(8):
        if game[i]==6:
            game[i]=" "
    if(value==5):
        return(1)
    else:
        return(2)
def player_computer(p1,p2):
    j=0
   
    for i in range (0,9):
        if(i+1)>8:
            break
        else:
            if(game[i]==p1 and game[i+1]==p1):
                #print("1")
                j=1
                if(i+2)%3 == 0:
                    if game[i-1]==" ":
                        game[i-1]=p2
                    else:
                        j=0
                        break
                else:
                    if game[i+2]==" ":
                        game[i+2]=p2
                    else:
                        j=0
                        break
           
                
                
                break
    if(j!=1):
        for i in range(0,9):
            if(i+3)>9:
                break
            else:
                if(game[i]==p1 and game[i+3]==p1):
                    #print("2")
                    j=1
                    if(i+6)> 9:
                        if game[i-3]==" ":
                            game[i-3]=p2
                        else:
                            j=0
                            break
                        
                        
                    else:
                        if game[i+6]==" ":
                            game[i+6]=p2
                        else:
                            j=0
                            break
                    
                    break
    if(j!=1):
        if(game[0]==game[4] and game[8]==" "):
            game[8]=p2
            j=1
        elif(game[0]==game[8] and game[4]==" "):
            game[4]=p2
            j=1
        elif(game[4]==game[8] and game[0]==" "):
            game[0]=p2
            j=1
        elif(game[2]==game[4] and game[6]==" "):
            game[6]=p2
            j=1
        elif(game[2]==game[6] and game[4]==" "):
            game[4]=p2
            j=1
        elif(game[4]==game[6] and game[2]==" "):
            game[2]=p2
            j=1
        else:
            j=0
   
                
                
                
        
    
      
    if(j!=1):
        #print("4")           
        t=random.randint(1,9)
        while True:
            
            if game[t-1]!=" ":
                t=random.randint(1,9)
            else:
                break
        game[t-1]=p2
    print_game()
    j=0
def draw(game):
    c=0
    
    for i in range(9):
        if game[i] != " ":
            c=c+1
    if(c==9 and q!=1):
        print("Match Draw")
        sys.exit()
print("The PAttern of tic toc is")
print("1 |2 |3")
print("__|__|__")
print("4 |5 |6")
print("__|__|__")
print("7 |8 |9")
begin()
