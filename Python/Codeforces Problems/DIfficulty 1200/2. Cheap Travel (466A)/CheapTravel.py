import math
i = input()

isplit = i.split()
n = int(isplit[0])
# n = Number of rides Ann has planned

m = int(isplit[1])
# m = Number of special ticket rides

a = int(isplit[2])
# a = Price of one ticket for a normal ride

b = int(isplit[3])
# b = Price of one ticket for a special ride

if n > m:
    specialNeed = n//m
    remainingRides = n - (m*specialNeed)
    specialPriceAll = specialNeed * b
    normalPriceAll = remainingRides * a
    totalPrice1 = specialPriceAll + normalPriceAll
    
    specialIFNeed = math.ceil(remainingRides/m)
    specialIFNeedPrice = specialIFNeed * m
    totalPrice2 = specialIFNeedPrice + normalPriceAll
    
    liste = [totalPrice1, totalPrice2]
    minimum = min(liste)
    print(minimum)

if m > n:
    totalPrice3 = n * a
    print(totalPrice3)