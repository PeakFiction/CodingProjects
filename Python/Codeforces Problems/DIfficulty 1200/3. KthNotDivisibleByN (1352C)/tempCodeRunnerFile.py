numberOfTestCase = int(input())
outputlist = []
Counter = 1
for i in range(numberOfTestCase):
    notDivisibleList = []
    query = input()
    queryListed = query.split()
    queryInput = [int(element) for element in queryListed]
    n = queryInput[0]
    k = queryInput[1]
    
    while len(notDivisibleList) != k:
        if Counter % n != 0:
            notDivisibleList.append(Counter)
            Counter = Counter + 1
        else:
            Counter = Counter + 1
            pass
    outputlist.append(notDivisibleList[-1])


for i in outputlist:
    print(i)