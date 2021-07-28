############################################################
# Largest K-Sum Sliding Window
############################################################
# Finds the largest sum of n adjacent values in an array
# This implmentation USES a sliding window algorithm
############################################################
__author__ = "Charles Qian"

import random

list = [random.randint(1, 20) for _ in range(100000)]

windowSize = 24
max = -9999
max_index = -9999
slidingSum = 0

print ("List has " + str (len(list)) + " items")
print ("Window size: " + str(windowSize))

for i in range(0,len(list)-windowSize):

    slidingSum += list[i]
    
    if i > windowSize - 1:
        slidingSum -= list[i-windowSize]
    
    if slidingSum > max:
        max = slidingSum
        max_index = i
    
print ("Largest Window Occurs at Index: ["+str(max_index) +"]: K-Sum "+ str(max))