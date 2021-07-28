
import string
import random

#Generate some random input to evaluate against
letters = string.ascii_lowercase
input =  ( ''.join(random.choice(letters) for i in range(1000)) )

def find_anagram(input, find):
    
    matching = {}
    match_count = 0
    
    #Populate our matcher dictionary
    for value in range(0, len(find)):
        if find[value] not in matching:
            matching[find[value]] = 1
        else:
            matching[find[value]] += 1
            
    print(matching)
    
    working_matcher = dict(matching)
    letters = len(find)
    
    #Begin evaluating our input string
    for i in range(0, len(input)):
    
        if input[i] in working_matcher and working_matcher[input[i]] != 0:
            working_matcher[input[i]] -= 1
            letters -= 1
        else:
            #Reset
            working_matcher = dict(matching)
            letters = len(find)
            
        if letters == 0:
            match_count += 1
            print("Anagram Detected!")
            
            #Reset
            working_matcher = dict(matching)
            letters = len(find)
        
find_anagram("banana aanbna many bananas do monkeys like to aaannb", "banana")


