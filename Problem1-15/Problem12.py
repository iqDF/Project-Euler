import math

""" PROBLEM 12
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
"""

import math

class BaseSolution():
    def __init__(self, n):
        print("initialise %s", self.__class__.__name__)

    def solve(self):
        print("solving...")

class BruteSolution(BaseSolution):
    """ Solve problem using brute force approach
    """

    def solve(self, N):
        #for each number in triangle sequences, find how many divisor they have
        #keep going but stop if any reach beyond 500 divisors'
        current = 10000
        while True:
            current_triangle = current*(current+1)//2
            n_divisors = self.count_divisors_simple(current_triangle)
            if n_divisors >= N:
                return current, current_triangle
            current+=1
            
    def count_divisors_simple(self, n):
        if n<2:
            return 1
        count = 2
        sqrt_n = int(math.sqrt(n))
        for i in range(2, sqrt_n+1):
            if n%i==0:
                if n//i == i:
                    count+=1
                else:
                    count+=2
        return count
        

class ImprovedBruteSolution(BaseSolution):
    def solve(self):
        current = 10000 #we guess the starting point :)
        while True:
            current_a, current_b = (current//2,current+1) if (current%2 == 0) else (current, (current+1)//2)
            n_divisors = self.__count_divisors_by_prime(current_a, current_b)
            if n_divisors >= N:
                return current, current_a *current_b
            current+=1
    
    def __count_divisors_by_prime(self, n1, n2):
        r = 0
        pf1 = self.__get_prime_factors(n1)
        pf2 = self.__get_prime_factors(n2)

        pf = {key: pf1.get(key, 0) + pf2.get(key, 0) for key in list(set(pf1.keys()).union(set(pf2.keys())))}
        for val in pf.values():
            r *= val+1 

        return r

    def __get_prime_factors(self, num):
        prime_factors = {}
        sqrt_num = int(math.sqrt(num))+1
        dic = {1:1}
        for i in range(2, sqrt_num+1):
            #counting
            if (i not in dic) and (num%i==0):
                log_i = int(math.log(num, i))
                if i**log_i:
                  return {i:log_i}
                for j in range(1, log_i+1):
                    k = i**j
                    if (num%k==0):
                        prime_factors[i] = j
                        continue
                    break
            #mark nonprime
            for j in range(i, sqrt_num+1, i):
                dic[j]=1
        
        for pf, exp in prime_factors.items():
            if exp==1:
              prime_factors[num//pf] = 1

        return prime_factors if prime_factors else {num:1}

                    


                        
                



