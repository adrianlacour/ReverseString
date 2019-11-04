#Author: Adrian LaCour
#Usage: palindrome("inputStingHere")

#function that returns the reverse of a string, using slicing
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    #Calling reverse function 
    rev = reverse(s) 
  
    #Checking if both string are equal 
    if (s == rev): 
        return True
    return False
  
  
# Test if a string is a palindrome
def palindrome(s):
    answer = isPalindrome(s)
    if answer == 1: #output true if t is a palindrome
        print("True") 
    else: 
        print("False")
        
#>>> palindrome("abba")
#True
#>>> palindrome("abababb")
#False
#>>> 
#>>> palindrome("abbba")
#True
