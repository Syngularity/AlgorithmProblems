import random

list = [random.randint(1, 20) for _ in range(100000)]

print ("list has " + str (len(list)) + " items")

windowSize = 50
max = -9999
max_index = -9999
slidingSum = 0

for i in range(0,len(list)-windowSize):

    slidingSum += list[i]
    
    if i > windowSize - 1:
        slidingSum -= list[i-windowSize]
    
    if slidingSum > max:
        max = slidingSum
        max_index = i
    
print ("Index: ["+str(max_index) +"]: "+ str(max))