############################################################
# Python Anagram Finder
############################################################
# Finds anagrams in random string input given a search word
# This implmentation doesn't fully use a sliding window
############################################################

import string
import random

#Generate some random input to evaluate against
letters = string.ascii_lowercase
input =  ( ''.join(random.choice(letters) for i in range(10000)) )

def find_anagram(input, find):
    
    print ("Searching for anagrams for [" + find + "]")
    
    matching = {}
    match_count = 0
    
    #Populate our matcher dictionary
    for char in find:
        matching[char] = matching[char] + 1 if char in matching else 1
            
    working_matcher = dict(matching)
    letters = len(find)
    
    #Begin evaluating our input string
    for i in range(0, len(input)):
    
        if input[i] in working_matcher and working_matcher[input[i]] != 0:
            working_matcher[input[i]] -= 1
            letters -= 1
        else:
            #Constraint broken - Reset
            working_matcher = dict(matching)
            letters = len(find)
            
        if letters == 0:
            match_count += 1
            
            #Pretty Print the found anagram and location within the string
            print("\tAnagram Detected! Index: " + str(i - len(find) + 1) + " (", end = "")
            for j in range (i - len(find) + 1, i + 1):
                print (input[j], end = "")
            print (")")
            
            #Match found! - Reset
            working_matcher = dict(matching)
            letters = len(find)
            
    print ("Total Matches: " + str(match_count))
        
find_anagram(input, "ant")


