############################################################
# Largest Simple Moving Average Sliding Window
############################################################
# Finds the largest simple moving average of n values in array
# This implmentation USES a sliding window algorithm
############################################################
__author__ = "Charles Qian"

import random

list = [random.randint(1, 20) for _ in range(15)]

def largest_sma(input, window):

    largest_sma = 0
    location = 0
    total = 0
    
    #Base Case
    for i in range(0, window):
        total = total + input[i] if total is not None else input[i]
        
    largest_sma = total/window
    
    #General Case
    for trailing_pointer, value in enumerate(input[window:], start = 0):
        
        #Add value entering window
        total = total + value
        
        #Remove value leaving window
        total = total - input[trailing_pointer]
        
        if total/window > largest_sma:
            largest_sma = total/window
            location = trailing_pointer + 1
            
    print("Largest SMA index[" + str(location) + "] " + str(largest_sma))

print (list)
largest_sma(list,3)