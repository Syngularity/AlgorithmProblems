############################################################
# Python Anagram Finder #2
############################################################
# Finds anagrams in random string input given a search word
# This implmentation USES a sliding window algorithm
############################################################
__author__ = "Charles Qian"

import string
import random

#Generate some random input to evaluate against
letters = string.ascii_lowercase
input =  ( ''.join(random.choice(letters) for i in range(20000)) )

def find_anagram(input, find):
    
    print ("Searching for anagrams for [" + find + "]")
    
    matching = {}
    match_count = 0
    
    #Populate our matcher dictionary
    for char in find:
        matching[char] = matching[char] + 1 if char in matching else 1
        
    run_match = {}
    
    #Begin evaluation our base case
    for index, value in enumerate(input[0:len(find)]):
        #Increment running matcher dictionary for this letter entering window
        run_match[value] = run_match[value] + 1 if value in run_match else 1
        
    if run_match == matching:
        #Pretty Print the found anagram and location within the string
        print("\tAnagram Detected! Index: 0 (", end = "")
        print (input[0:len(find)], end = "")
        print (")")
        match_count += 1
    
    #Begin evaluating general case
    for trailing_pointer, value in enumerate(input[len(find):], start = 0):
   
        #Increment running matcher dictionary for this letter entering window
        run_match[value] = run_match[value] + 1 if value in run_match else 1
        
        #Decrement running matcher dictionary for this letter leaving window
        run_match[input[trailing_pointer]] = run_match[input[trailing_pointer]] - 1 
        if run_match[input[trailing_pointer]] == 0:
            del run_match[input[trailing_pointer]]

        if run_match == matching:
            #Pretty Print the found anagram and location within the string
            print("\tAnagram Detected! Index: " + str(trailing_pointer + 1) + " (", end = "")
            for j in range (trailing_pointer + 1 , trailing_pointer + len(find) + 1):
                print (input[j], end = "")
            print (")")
            match_count += 1

    print ("Total Matches: " + str(match_count))
        
find_anagram(input, "ant")


