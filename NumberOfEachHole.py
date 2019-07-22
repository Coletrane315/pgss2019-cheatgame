#for i in range (0,a):
    #    print("1 ");

handSize = 0

#Number of cards you're missing in sequence (e.g. if you have one of every number but two, that's one "hole").
holeCount = 0

#calculates factorials
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1);

#Combinatorial function
def combination(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k));

#Variables to find the number of sequences with n holes.
zeroHoleCount = 0
oneHoleCount = 0
twoHoleCount = 0
threeHoleCount = 0
fourHoleCount = 0
fiveHoleCount = 0
sixHoleCount = 0
sevenHoleCount = 0
eightHoleCount = 0
nineHoleCount = 0

#HoleCounter Method
def numberOfEachHoles(holeCount):
    if holeCount == 0:
        zeroHoleCount += 1
    elif holeCount == 1:
        oneHoleCount += 1
    elif holeCount == 2:
        twoHoleCount += 1
    elif holeCount == 3:
        threeHoleCount += 1
    elif holeCount == 4:
        fourHoleCount += 1
    elif holeCount == 5:
        fiveHoleCount += 1
    elif holeCount == 6:
        sixHoleCount += 1
    elif holeCount == 7:
        sevenHoleCount += 1
    elif holeCount == 8:
        eightHoleCount += 1
    elif holeCount == 9:
        nineHoleCount += 1
        
for a in range (0,4):
    handSize += a

    if a == 0:
        holeCount += 1

    if handSize == 13:
        numberOfEachHoles(holeCount)
    
    for b in range (0,4):
       handSize += b
       if b == 0:
           holeCount += 1

       if handSize == 13:
           numberOfEachHoles(holeCount) 

       for c in range (0,4):
           handSize += c
           if c == 0:
               holeCount += 1

           if handSize == 13:
               numberOfEachHoles(holeCount) 

           for d in range (0,4):
               handSize += d
               if d == 0:
                   holeCount += 1

               if handSize == 13:
                   holeCount += 9
                   numberOfEachHoles(holeCount) 

               for e in range (0,4):
                   handSize += e
                   if e == 0:
                       holeCount += 1

                   if handSize == 13:
                       holeCount += 8
                       numberOfEachHoles(holeCount) 
                   for f in range (0,4):
                       handSize += f
                       if f == 0:
                           holeCount += 1
                       if handSize == 13:
                           holeCount += 7
                           numberOfEachHoles(holeCount) 
                       for g in range (0,4):
                           handSize += g
                           if g == 0:
                               holeCount += 1

                           if handSize == 13:
                               holeCount += 6
                               numberOfEachHoles(holeCount) 

                           for h in range (0,4):
                               handSize += h
                               if h == 0:
                                  holeCount += 1

                               if handSize == 13:
                                   holeCount += 5
                                   numberOfEachHoles(holeCount) 

                               for i in range (0,4):
                                   handSize += i
                                   if i == 0:
                                       holeCount += 1

                                   if handSize == 13:
                                      holeCount += 4
                                      numberOfEachHoles(holeCount) 

                                   for j in range (0,4):
                                       handSize += j
                                       if j == 0:
                                          holeCount += 1

                                       if handSize == 13:
                                          holeCount += 3
                                          numberOfEachHoles(holeCount) 

                                       for k in range (0,4):
                                          handSize += k
                                          if k == 0:
                                              holeCount += 1

                                          if handSize == 13:
                                              holeCount += 2
                                              numberOfEachHoles(holeCount) 

                                          for l in range (0,4):
                                              handSize += l
                                              if l == 0:
                                                  holeCount += 1

                                              if handSize == 13:
                                                  holeCount += 1
                                                  numberOfEachHoles(holeCount) 

                                              for m in range (0,4):
                                                  handSize += m
                                                  if m == 0:
                                                      holeCount += 1

                                                  if handSize == 13:
                                                      if holeCount == 0:
                                                          zeroHoleCount += 1
                                                      elif holeCount == 1:
                                                          oneHoleCount += 1
                                                      elif holeCount == 2:
                                                          twoHoleCount += 1
                                                      elif holeCount == 3:
                                                          threeHoleCount += 1
                                                      elif holeCount == 4:
                                                          fourHoleCount += 1
                                                      elif holeCount == 5:
                                                          fiveHoleCount += 1
                                                      elif holeCount == 6:
                                                          sixHoleCount += 1
                                                      elif holeCount == 7:
                                                          sevenHoleCount += 1
                                                      elif holeCount == 8:
                                                          eightHoleCount += 1
                                                      elif holeCount == 9:
                                                          nineHoleCount += 1
                                                  else:
                                                      holeCount = 0
                                                      handSize = 0

print(zeroHoleCount)
print(oneHoleCount)
print(twoHoleCount)
print(threeHoleCount)
print(fourHoleCount)
print(fiveHoleCount)
print(sixHoleCount)
print(sevenHoleCount)
print(eightHoleCount)
print(nineHoleCount)                                                  
        
        
    
    
