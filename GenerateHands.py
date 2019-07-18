import random

numPlayers = int(input("How many players are there playing?: "))
handSize = int(52 / numPlayers)
totalProb = 0

numPerfect = 0

for j in range(1, handSize + 1):
    for i in range(100000):
        hand = []
        perfectSeq = True
        
        for j in range(1, handSize + 1):
            x = random.randint(1,52)
            hand.append(x)
            if(x > 4 * handSize):
                perfectSeq = False
                
        if(perfectSeq == True):
           shouldContinue = True
        else:
            shouldContinue = False
            
        for k in range(1, j +  1):
            if(shouldContinue == True):
                isNumberThere = False
                for l in hand:
                    if (l == k or l == 13 + k or l == 26 + k or l == 39 + k):
                        isNumberThere = True
                if(isNumberThere == False):
                    perfectSeq = False
                    shouldContinue = False
            else:
                break

        if(perfectSeq == True):
           numPerfect += 1
             
    totalProb += (numPerfect / 1000000.0)

print(totalProb)

