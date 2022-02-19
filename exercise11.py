from cmath import log
import json
from urllib.request import Request, urlopen



#-----------------------------------Get-Data-------------------------------------#
def getlatestround():
    req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    datadict=json.loads(data)
    return datadict.get('round')

    
def getrandoms(round):
    url="https://drand.cloudflare.com/public/"
    url=url+str(round)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    datadict=json.loads(data)
    return datadict.get('randomness')



#-----------------------------------Conversions-------------------------------------#
def strtohex(list):
    for i in range(20):
        list[i]=int(list[i],16)
        list[i]=hex(list[i])
    return list

def converttostring(list):
    string=""
    for i in range(20):
        temp=str(list[i])
        string+=temp
    return string



#-----------------------------------Entropy-------------------------------------#
def findchances(str):
    timesfound=findcharoccurances(str)
    chancelist=[0 for i in range(16)]
    for i in range(16):
        chancelist[i]=timesfound[i]/len(str)
    return chancelist
    
def findcharoccurances(str):
    hexlist=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    timesfound=[0 for i in range(16)]
    for i in range(len(hexlist)):
        for j in range(len(str)):
            if str[j]==hexlist[i]:
                timesfound[i]+=1
    return timesfound

def findentropy(str):
    chancelist=findchances(str)
    sum=0
    for i in range(16):
        chance=chancelist[i]
        sum=sum-(chance*log(chance,2))

    return sum
    
#-----------------------------------Main-------------------------------------#
def main():
    randomslist=[0 for i in range(20)]              
    rounds=[0 for i in range(20)]
    rounds[0]=getlatestround()
    for i in range (20):
        rounds[i]=rounds[0]-i

    index=0
    for round in (rounds):
        randomslist[index]=getrandoms(round)
        index+=1

    randomslist=strtohex(randomslist)

    mystring=converttostring(randomslist)
    entropy=findentropy(mystring)
    print("Entropy Of String is:",entropy)


main()