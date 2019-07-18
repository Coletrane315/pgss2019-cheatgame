import random

handSize = 8
numPerfect = 0
arr = []

for i in range(1000):
    for j in range(handSize):
        check = True
        x = random.randint(1,52)
        arr.append(x)
        if(x > 4 * handSize):
            check = False

    for k in range(handSize):
        isNumberThere = False
        for l in arr:
            if (l == k):
                isNumberThere = True
        if(isNumberThere == False):
            check = False

    if(check == True):
       numPerfect += 1
                
        

print (numPerfect / 1000.0)
