#import matplotlib.pyplot as plt


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
f = open("primes.json", "r")
#rstrip() removing trailing \n
primes = f.read().rstrip().split(",")

fractions = []
#Define Fractions
for prime in primes:
    iprime = int(prime)
    mayFraction = 1/(iprime)
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
print(result)


#Plotting




