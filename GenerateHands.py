import random

numPlayers = float(input("How many players are there playing?: "))
handSize = round(52/numPlayers)

numPerfect = 0
hand = []

for i in range(1000):
    for j in range(handSize):
        check = True
        x = random.randint(1,52)
        hand.append(x)
        if(x > 4 * handSize):
            check = False

    for k in range(handSize):
        isNumberThere = False
        for l in hand:
            if (l == k):
                isNumberThere = True
        if(isNumberThere == False):
            check = False

    if(check == True):
       numPerfect += 1
             

print (numPerfect / 1000.0)
