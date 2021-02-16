#!/usr/bin/python
import matplotlib.pyplot as plt
from numpy import pi
from math import ceil
import sys
import datetime

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
    #print(str(result) + "\n")
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

def summary(array, separation):
    output = []
    num = 0
    while num < len(array):
        output.append(array[num])
        num = num + separation
    return output


userInput = sys.argv[1]
# userInput = 150000
separation = int(sys.argv[2])
# separation = 100

try:
    userInt = int(userInput) 
except ValueError:
    print("Error: Tria un enter positiu si us plau")
    exit()


begin_time = datetime.datetime.now()
llistaPrimers = summary(computePrimes(userInt), separation)
print(f"Time taken to calculate {len(llistaPrimers)} primes: {datetime.datetime.now() - begin_time}")

begin_time6 = datetime.datetime.now()
pies0 = [computePi(prime) for prime in range(len(llistaPrimers))]
print(f"Time taken to calculate pi-es: {datetime.datetime.now() - begin_time6}")

usedPrimes0 = [num for num in range(len(llistaPrimers))]

begin_time5 = datetime.datetime.now()
usedPrimes = summary(llistaPrimers, separation)
pies = summary(pies0, separation)
print(f"Time taken to summarize: {datetime.datetime.now() - begin_time5}")

begin_time2 = datetime.datetime.now()
#Plotting
yMin = 3.09
yMax = 3.21
plt.axis(ymin=yMin, ymax=yMax)
plt.plot(usedPrimes, pies, 'b-')
plt.plot(int(userInput), [pi]*len(userInput), 'r-')
plt.ylabel('Calculated π')
plt.xlabel('Number of primes used')
print(f"Time taken to plot chart: {datetime.datetime.now() - begin_time2}")
begin_time3 = datetime.datetime.now()
plt.show()
print(f"Time taken to plt.show: {datetime.datetime.now() - begin_time3}")
print(f"Time taken total: {datetime.datetime.now() - begin_time}")
