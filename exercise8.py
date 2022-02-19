from random import choice


#-----------PlayerLocations-----------#

def InitializePlayer1Location(rows,cols):
    Player1Location=[0,0]
    for i in range(2):
       Player1Location[i]=GenerateRandomNumber(rows,cols)
    return Player1Location


def InitializePlayer2Location(rows,cols):
    Player2Location=[0,0]
    for i in range(2):
        Player2Location[i]=GenerateRandomNumber(rows,cols)
    return Player2Location


#-----------RandomNum-----------#
def GenerateRandomNumber(rows,cols):
    sequence = [i for i in range(0,20)]
    selection = choice(sequence)
    while (selection>=rows or selection>=cols):
        if (selection<rows and selection<cols):
            return selection
        selection = choice(sequence)
    return selection
        

#-----------PlayerChecks-----------#
def Bishop(rows,cols):
    #Primary Diagonal
    offset=Player2Location[1]-Player2Location[0]    #j-i
    for i in range(rows):
        for j in range(cols):
            if (i+offset) == j:
                if Locationlist[i][j] == 1:
                    return True

    #Secondary Diagonal
    offset=Player2Location[0]+Player2Location[1]
    for i in range(rows):
        for j in range(cols):
            if (i+j) == offset:
                if Locationlist[i][j] == 1:
                    return True

    return False


def Rook(Player1Location,rows,cols):
    for i in range(rows):
        for j in range(cols):
            if Locationlist[i][Player1Location[1]] == 2:        #Player1Location[0]=Row     Player1Location[1]=Col
                return True
            elif Locationlist[Player1Location[0]][j] == 2:
                return True
    return False


def InitializeList(rows,cols):
    list = [[0 for i in range(cols)] for j in range(rows)]
    return list



##################################################################################


rows, cols = (8, 8)
ScoreList=[0,0]                  
ScoreList1=[0,0]      #For Game 1            8x8
ScoreList2=[0,0]      #For Game 2            7x7
ScoreList3=[0,0]      #For Game 3            7x8
round=0


while(round<100):
    Locationlist = InitializeList(rows,cols)
    PlayerLocations=[[0]*2]*2   #Location for player1 and player2
    Player1Location=InitializePlayer1Location(rows,cols)
    Player2Location=InitializePlayer2Location(rows,cols)

    while Player1Location[0]==Player2Location[0] and Player1Location[1]==Player2Location[1]:
        Player1Location=InitializePlayer1Location(rows,cols)
        Player2Location=InitializePlayer2Location(rows,cols)

    Locationlist [Player1Location[0] ] [ Player1Location[1] ]=1     #Rook Player 1
    Locationlist [Player2Location[0] ] [ Player2Location[1] ]=2     #Knight Player 2


    if Rook(Player1Location,rows,cols)==True:
        ScoreList1[0]+=1
    elif Bishop(rows,cols)==True:
        ScoreList1[1]+=1

    if round==99:
        print("FOR GAME:",rows,"x",cols)
        print("Player 1 Score (Rook)  :",ScoreList1[0])
        print("Player 2 Score (Bishop):",ScoreList1[1])
        print("")
        
    round=round+1
    


ScoreList=[0,0] 
rows, cols = (7, 7)

while(round<200):
    Locationlist = InitializeList(rows,cols)
    PlayerLocations=[[0]*2]*2   #Location for player1 and player2
    Player1Location=InitializePlayer1Location(rows,cols)
    Player2Location=InitializePlayer2Location(rows,cols)

    while Player1Location[0]==Player2Location[0] and Player1Location[1]==Player2Location[1]:
        Player1Location=InitializePlayer1Location(rows,cols)
        Player2Location=InitializePlayer2Location(rows,cols)

    Locationlist [Player1Location[0]][Player1Location[1]]=1     #Rook Player 1
    Locationlist [Player2Location[0]][Player2Location[1]]=2     #Knight Player 2


    if Rook(Player1Location,rows,cols)==True:
        ScoreList2[0]+=1
    elif Bishop(rows,cols)==True:
        ScoreList2[1]+=1


    if round==199:
        print("FOR GAME:",rows,"x",cols)
        print("Player 1 Score (Rook)  :",ScoreList2[0])
        print("Player 2 Score (Bishop):",ScoreList2[1])
        print("") 

    round=round+1


ScoreList=[0,0]   
rows, cols = (7,8)

while(round<300):
    Locationlist = InitializeList(rows,cols)
    PlayerLocations=[[0]*2]*2   #Location for player1 and player2
    Player1Location=InitializePlayer1Location(rows,cols)
    Player2Location=InitializePlayer2Location(rows,cols)

    while Player1Location[0]==Player2Location[0] and Player1Location[1]==Player2Location[1]:
        Player1Location=InitializePlayer1Location(rows,cols)
        Player2Location=InitializePlayer2Location(rows,cols)

    Locationlist [Player1Location[0] ] [ Player1Location[1] ]=1     #Rook Player 1
    Locationlist [Player2Location[0] ] [ Player2Location[1] ]=2     #Knight Player 2


    if Rook(Player1Location,rows,cols)==True:
        ScoreList3[0]+=1
    elif Bishop(rows,cols)==True:
        ScoreList3[1]+=1

    if round==299:
        print("FOR GAME:",rows,"x",cols)
        print("Player 1 Score (Rook)  :",ScoreList3[0])
        print("Player 2 Score (Bishop):",ScoreList3[1])
        print("")
        
    round=round+1




for i in range(2):
    ScoreList[i]=ScoreList1[i]+ScoreList2[i]+ScoreList3[i]

print("Score For All Games: ")
print("Player 1 Score (Rook)    :",ScoreList[0])
print("Player 2 Score (Bishop)  :",ScoreList[1])
print("")

if(ScoreList[0]>ScoreList[1]):      # Player1 Score > Player2 Score
    print("Player 1 Is The Winner")
elif (ScoreList[0]<ScoreList[1]): 
    print("Player 2 Is The Winner")
else:
    print("No Winner")

