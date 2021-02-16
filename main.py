#!/usr/bin/python
import matplotlib.pyplot as plt
from numpy import pi
from math import ceil
import sys

def divBy4(n):
    if ((n-1) % 4 == 0):
        return True
    else:
        return False

def massiveProduct(list):
    output = 1
    for i in list:
        output = output*i
    return output

def computePi(nOfPrimes):
    fractions = []
    #Define Fractions
    for prime in primes:
        iprime = int(prime)
        mayFraction = 1/(iprime)
        if primes.index(prime) == nOfPrimes:
            break
        if divBy4(iprime):
            fractions.append(mayFraction)
        else:
            fractions.append(-mayFraction)

    finalFractions = []
    #Compute pi
    for fraction in fractions:
        newFraction = 1+fraction
        finalFractions.append(newFraction)

    result = 2/(massiveProduct(finalFractions))
    print(str(result) + "\n")
    return result
    
def isDivisble(a, b):
    if a%b == 0:
        return True
    else:
        return False


def isPrime(candidate):
    global primes
    if candidate == 0:
        return False
    elif candidate < 4:
        return True
    else: 
        sqrtN = ceil(candidate**(1/2))
        for i in primes:
            if sqrtN < i:
                return True
            elif i == 1:
                continue
            elif isDivisble(candidate, i):
                return False
        return True


def computePrimes(maxPrime):
    global primes
    primes = []
    for i in range(maxPrime):
        if isPrime(i):
            primes.append(i)
    return primes


userInput = sys.argv[1]
try:
    userInt = int(userInput) 
except ValueError:
    print("Error: Tria un enter positiu si us plau")
    exit()

fprimes = computePrimes(userInt)


pies = [computePi(prime) for prime in range(len(fprimes))]

usedPrimes = [num for num in range(len(fprimes))]


#Plotting
yMin = 3.09
yMax = 3.21
plt.axis(ymin=yMin, ymax=yMax)
plt.plot(usedPrimes, pies, 'b-')
plt.plot(usedPrimes, [pi]*len(primes), 'r-')
plt.ylabel('Calculated π')
plt.xlabel('Number of primes used')
plt.show()
