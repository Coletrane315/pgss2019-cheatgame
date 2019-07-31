
class SeqProbabilityCalculator:

    #Combinatorial function
    def combination(self,n,k):
        import math
        if(n >= k):
            return math.factorial(n)/(math.factorial(k)*math.factorial(n-k));
        else:
            return 0


    def calculateEvents(self,num_holes,max_holes,hand_size):
        ls = []
        i = max_holes
        while(i >= num_holes):
            probability = self.combination(4*(hand_size-i),hand_size)*self.combination(hand_size,i)
            for times in range(1,max_holes-i+1):
                 probability = probability - self.combination(i+times,i)*ls[max_holes-i-times]
            ls.append(probability)
            i = i-1
        return ls[max_holes-num_holes]

            
    def calculateProbability(self,num_players):
        import math
        hand_size = int(52/num_players)
        probability = []
        max_holes = hand_size-int(math.ceil(hand_size/4))
        multiplier = 1
        for num in range(0,max_holes+1):
            probability.insert(0,multiplier * self.calculateEvents(num,max_holes,hand_size)/self.combination(52,hand_size))
        sum = 0 
        for i in probability:
            sum = sum + i
        print(sum)
        return probability
        
    def recursion(self,num_holes,max_holes,hand_size):           
        if(num_holes == max_holes):
            return self.combination(4*(hand_size-num_holes),hand_size)*self.combination(hand_size,num_holes)
        else:
            probability = self.combination(4*(hand_size-num_holes),hand_size)*self.combination(hand_size,num_holes)
            for times in range(1,max_holes-num_holes+1):
                probability = probability - self.combination(num_holes+times,num_holes)*self.recursion(num_holes+times,max_holes,hand_size)
            return probability


    def probabilityWinInNTurns(num_players):
        probabilities = x.calculateProbabilities(num_players)
        sum_prob = 0
        threshold_of_lies = 3
        for i in range (0,threshold + 1):
            sum_prob = sum_prob + probabilities[i]
        return sum_prob
    
