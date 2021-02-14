import matplotlib.pyplot as plt
from numpy import pi
from math import ceil


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
    return result
    
def isDivisble(a, b):
    if a%b == 0:
        return True
    else:
        return False

def isPrime(candidate):
    if candidate < 4:
        return True
    y = ceil(candidate**(1/2))
    for i in range(2, int(y)+1):
        if isDivisble(candidate, i):
            return False
    return True


def computePrimes(maxPrime):
    primes = []
    for i in range(1, maxPrime):
        if isPrime(i):     
            primes.append(i)
    return primes

testPrimes = computePrimes(10000)
print(testPrimes)
######
f = open("primes.json", "r")
    #rstrip() removing trailing \n
primes = f.read().rstrip().split(",")
#######
#Generate pi-s
# pies = []
# for prime in range(len(primes)):
#     pies.append(computePi(prime))

pies = [computePi(prime) for prime in range(len(primes))]

#Generate nº of primes
usedPrimes = [num for num in range(999)]

#Plotting

yMin = 3.09
yMax = 3.21
plt.axis(ymin=yMin, ymax=yMax)
plt.plot(usedPrimes, pies, 'b-')
plt.plot(usedPrimes, [pi]*999, 'r-')
plt.xlabel('Calculated π')
plt.ylabel('Number of primes used')
# ax = plt.figure().add_subplot(111)
# ax.plot(usedPrimes, pies, c='b', label='y1', linewidth=3)
plt.show()