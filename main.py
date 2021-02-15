import matplotlib.pyplot as plt
from numpy import pi
from math import ceil
import concurrent.futures
import threading

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


def computePrimes(minPrime, maxPrime, thread):
    print(f"Started calculating thread {thread}")
    primes = []
    for i in range(minPrime, maxPrime):
        if isPrime(i):   
            print(i)  
            primes.append(i)
    return primes

primes = [] 
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     primes.append(computePrimes(3, 25000, 1))
#     primes.append(computePrimes(25000, 50000, 2))
#     primes.append(computePrimes(50000, 75000,3))
prim1 = threading.Thread(target=computePrimes(3, 25000, 1))
prim2 = threading.Thread(target=computePrimes(25000, 50000, 2))
prim1.start()
prim2.start()

#Compress list of lists into list
primes = [item for list in primes for item in list]

pies = [computePi(prime) for prime in range(len(primes))]

usedPrimes = [num for num in range(len(primes))]


#Plotting
yMin = 3.09
yMax = 3.21
plt.axis(ymin=yMin, ymax=yMax)
plt.plot(usedPrimes, pies, 'b-')
plt.plot(usedPrimes, [pi]*len(primes), 'r-')
plt.xlabel('Calculated π')
plt.ylabel('Number of primes used')
plt.show()