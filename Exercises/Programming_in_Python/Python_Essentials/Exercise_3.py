#Write a function that takes a string as an argument and returns the 
#number of capital letters in the string

def count_caps(stringin):
    count=0
    for letter in stringin:
        if letter==letter.upper():
            count += 1
            
    return count

