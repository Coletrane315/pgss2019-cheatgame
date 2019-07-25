
class SeqProbabilityCalculator:


    #calculates factorials
    def factorial(self,n):
        return 1 if (n==1 or n==0) else n * self.factorial(n-1);

    #Combinatorial function
    def combination(self,n,k):
        return self.factorial(n)/(self.factorial(k)*self.factorial(n-k));


    def calculateEvents(self,num_holes,max_holes,hand_size):
        ls = []
        i = max_holes
        while(i >= num_holes):
            probability = self.combination(4*(hand_size-i),hand_size)*self.combination(hand_size,i)
            for times in range(1,max_holes-i+1):
                 probability = probability - self.combination(i+times,i)*ls[times-1]
            ls.append(probability)
            i = i-1
        return ls[max_holes-num_holes]

            
    def calculateProbability(self,num_players):
        import math
        hand_size = int(52/num_players)
        probability = []
        max_holes = 13-int(math.ceil(hand_size/4))
        for num in range(0,max_holes):
            probability.append(self.calculateEvents(num, max_holes,hand_size))
        return probability
        
    def recursion(self,num_holes,max_holes,hand_size):           
        if(num_holes == max_holes):
            return self.combination(4*(hand_size-num_holes),hand_size)*self.combination(hand_size,num_holes)
        else:
            probability = self.combination(4*(hand_size-num_holes),hand_size)*self.combination(hand_size,num_holes)
            for times in range(1,max_holes-num_holes+1):
                probability = probability - self.combination(num_holes+times,num_holes)*self.recursion(num_holes+times,max_holes,hand_size)
            return probability

