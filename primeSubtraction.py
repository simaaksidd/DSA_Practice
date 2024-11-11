# PROBLEMS: Leetcode 2601, ...

# Leetcode 2601: 
# First we will use the brute force solution to understand the problem. 

# Brute force: 
# for each element, minimize the elements such that it is greater than the prev element and smaller than the next element.
# to do this we find the largest prime to subtract from each element. 
def primeSubOperation(nums):
    prev = 0
    #O(sqrt(n))
    def isPrime(num):
        root = int(num ** 0.5) # sqrting the number for efficiency
        for i in range(2, root+1):
            if num % i == 0:
                return False
        return True
    
    # O(n)
    for i in nums:
        ub = i - prev # make an upper bound so that we do not go larger smaller than the prev value
        largest = 0
        
        #O(m) where m is proportional to n 
        for j in reversed(range(2, ub)):
            if isPrime(j): 
                largest = j
                break
            
        if i - largest <= prev:
            return False
        prev = i - largest
    return True

# this solution is fine for smaller inputs, but if numbers get large, then the main operation could take very long
# time complexity is O(n * m * sqrt(n))

# how do we get rid of repeated work? 
'''
        for j in reversed(range(2, ub)):
        
            if isPrime(j):  this line is repeated work
                            Say we have a ub, then we are constantly computing isPrime for [2,ub]
                            to fix this, lets just compute the primes such that we find all primes one then store it. 


                largest = j
                break
'''
'''
# primes[i] == True if i == prime 
primes = [False, False] 
for i in range(2, max(nums)):
    if isPrime(i):
        primes.append(True)
    else:
        primes.append(False)

for i in nums:
    ub = i - prev # make an upper bound so that we do not go larger smaller than the prev value
    largest = 0
    
    for j in reversed(range(2, ub)):
        if primes[i]: # instead of an O(~n^2) compute, we are doing an O(n) array lookup
            largest = j
            break
        
    if i - largest <= prev:
        return False
    prev = i - largest
return True
'''

# We are not done!
# I want primes[i] to be equal to the largest prime that is <= to i
# if I had an array like this, I can just fine the prime with the idx ub-1


'''
primes = [0, 0] # instead of using a boolean value, we can find for each number to ub the LARGEST prime that can subtract it. 
# we need the base cases of 0 and 1 to be 0, then for 2 it is 2, then for 3 it is 3, then for 4 it is 4, and so on 

# a dry run of the algo will look like this: [0, 0, 2, 3, 3, 5, 5, 7, 7, 7, ...]

# lets say we are asking if 7 is prime because 7 is the largest prime in the primes list 
i = 7  is 7 prime? Since it is, and it is the largest prime given the ub, we can just return that value. 
if it is not, then the largest prime <= 7 is the same as the largest prime <= 6

for i in range(2, max(nums)):
    if isPrime(i):
        primes.append(i) # instead of appending T or F, we append the prime itself if it is prime
    else:
        primes.append(primes[i-1]) # if it is not prime, then we append the previous value that is prime

for i in nums:
    ub = i - prev # make an upper bound so that we do not go larger smaller than the prev value
    largest = 0
    
    for j in reversed(range(2, ub)):
        if primes[i]: # instead of an O(~n^2) compute, we are doing an O(n) array lookup
            largest = j
            break
        
    if i - largest <= prev:
        return False
    prev = i - largest
return True
'''

# with all of this new work, we have a final time complexity of O(n + m * sqrt(m))

# So the final code will be: 


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def isPrime(num):
            root = int(num ** 0.5)
            for i in range(2, root+1):
                if num % i == 0:
                    return False
            return True

        primes = [0, 0]
        for i in range(2, max(nums)):
            if isPrime(i):
                primes.append(i)
            else:
                primes.append(primes[i-1])
        
        prev = 0
        for i in nums:
            ub = i - prev 
            largest = primes[ub - 1]
            if i - largest <= prev:
                return False
            prev = i - largest
        return True