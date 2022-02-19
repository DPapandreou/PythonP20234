from ast import While
import pprint
from random import choice


#-----------List Initializations-----------#
def InitializeList(rows,cols,items):
    list = [[[0 for z in range(items)]for j in range(cols)]for i in range(rows)]        ##3D LIST 3*3*3   For each Cell of the third dimension , the Index is valued from 0 to 2 , that corresponds to Small Medium Large and for each of those indexes the content is as follows
    return list                                                                         ##  0-> No ring Present     1->Ring Present

def InitializeStepList():
    list=[0 for i in range(100)]
    return list


#-----------RandomNumbers----------------#
def GenerateRandomLocation(rows,cols):
    sequence = [i for i in range(0,10)]
    selection = choice(sequence)
    while (selection>=rows or selection>=cols):
        if (selection<rows and selection<cols):
            return selection
        selection = choice(sequence)
    return selection

def GenerateRingSize():
    sequence = [0,1,2]
    selection = choice(sequence)
    return selection


#--------------RandomPlace-----------------------#
def PlaceRing(LocationList):
    row=GenerateRandomLocation(3,3)
    col=GenerateRandomLocation(3,3)
    ring=GenerateRingSize()
    while(LocationList[row][col][ring]==1):
        row=GenerateRandomLocation(3,3)
        col=GenerateRandomLocation(3,3)
        ring=GenerateRingSize()

    LocationList[row][col][ring]=1
    
    return LocationList



#-------------------------------------Check List For Same Sized Rings-------------------------------------#

#Checks the diagonals for a Specified Ring Size called Item, item ranges from 0 to 2 representing a size of small to large
def DiagonalItemCheck(Locationlist,item):                  
    #Primary Diagonal
    count=0
    for i in range(3):
        for j in range(3):
            if i==j and Locationlist[i][j][item]!=0:
                count+=1
    if count==3:
            return True
    else:
        count=0

    #Secondary Diagonal
    for i in range(3):
        for j in range(3):
            if i+j==2 and Locationlist[i][j][item]!=0:
                count+=1
    if count==3:
            return True
    else:
        count=0

    return False


#Checks the Rows and Columns for a Specified Ring Size called Item, item ranges from 0 to 2 representing a size of small to large
def RowColItemCheck(Locationlist,item):                 
    #Row Check
    for i in range(3):
        count=0
        for j in range(3):
            if Locationlist[i][j][item]!=0:
                count+=1
        if count==3:
            return True

    #Column Check
    for j in range(3):
        count=0
        for i in range(3):
            if Locationlist[i][j][item]!=0:
                count+=1
        if count==3:
            return True

    return False



#---------------------------------Check List For Rings Sized From Small To Large----------------------------------#

#Checks the Rows and Cols for Rings Sized from small to large , from 0(Small) to 2 (Large)
def RowColCheck(LocationList):
    #Row Check
    for i in range(3):
        count=0
        for j in range(3):
            if LocationList[i][j][j]!=0:        
                count+=1
        if count==3:
            return True

    #Column Check
    for j in range(3):
        count=0
        for i in range(3):
            if LocationList[i][j][i]!=0:        
                count+=1
        if count==3:
            return True
    return False


#Checks the diagonals for Rings Sized from small to large , from 0(Small) to 2 (Large)
def DiagonalCheck(Locationlist):  
    #Primary Diagonal
    count=0
    for i in range(3):
        for j in range(3):
            if i==j and LocationList[i][j][j]!=0:
                count+=1
    if count==3:
            return True
    else:
        count=0

    #Secondary Diagonal
    for i in range(3):
        for j in range(3):
            if i+j==2 and Locationlist[i][j][i]!=0:
                count+=1
    if count==3:
            return True
    else:
        count=0

    return False



#---------------------------------Win Conditions Check----------------------------------#

def CheckWinCondition1(LocationList):               ##Same Sized Rings in the same Row or Col or Diagonal 
    for item in range(3):
                if RowColItemCheck(LocationList,item)==True:
                    return True
                elif DiagonalItemCheck(LocationList,item)==True:
                    return True
    return False


def CheckWinCondition2(LocationList):               ##Rings Sized From Small to Large in the same Row/Col or Diagonal 
    if RowColCheck(LocationList)==True:
        return True
    elif DiagonalCheck(LocationList)==True:
        return True
    return False






#-----------------------------------Main Program---------------------------------------------------------#

StepList=InitializeStepList()           ## A list that holds each rounds steps
LocationList=InitializeList(3,3,3)      ## 3D list with each cell being a 3 item list with indexes from 0 to 2 corresponding to the ring sized and with a value of 0 if no ring is present and 1 if ring is present

for round in range(100):                ## For each Round the LocationList and steps are returned to their original values
    win=False
    steps=0
    LocationList=InitializeList(3,3,3)    

    while(win==False):
        LocationList=PlaceRing(LocationList)
        steps+=1
        if CheckWinCondition1(LocationList)==True or CheckWinCondition2(LocationList)==True:
            print("Round",round+1,"Won in",steps,"Steps")
            win=True
            StepList[round]=steps
            pprint.pprint(LocationList)
        
    

sum=sum(StepList)
AvgSteps=sum/round
print("Average Steps For 100 Rounds:",AvgSteps)
pprint.pprint(LocationList)