"""
Sum of Digits / Digital Root
Instructions
In this kata, you must create a digital root function.
A digital root is the recursive sum of all the digits in a number. Given n, 
take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6
"""

# this is a good opportunity for recursion
def digital_root(n):
    # convert n to str to separate integers 
    # into list, add result
    integers = [int(i) for i in str(n)]
    summation = sum(integers)
    
    # recursive function
    # keep running function until 
    # a single integer is returned
    if len(str(summation)) > 1:
        print(summation)
        summation = digital_root(summation)
        return(summation)
    
    elif len(str(summation)) == 1:
        print(summation)
        return(summation)
    
####################
## BEST PRACTICES ##
####################
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

a = digital_root(942768)
print(a)
        