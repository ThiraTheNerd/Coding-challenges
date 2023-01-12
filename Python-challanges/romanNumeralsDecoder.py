# Create a function that takes a Roman numeral as its argument and 
# returns its value as a numeric decimal integer. 
# You don't need to validate the form of the Roman numeral.

# Modern Roman numerals are written by expressing each decimal digit of the number
# to be encoded separately, starting with the leftmost digit and skipping any 0s.
# So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered
# "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", 
# uses each letter in descending order.

# Example:

# solution('XXI') # should return 21
# Help:

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

def solution(roman):
    #create a map of the roman numbers
    roman_no={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    n = len(roman)
    i = n-1
    output = 0
    #Loop through the roman from the back foward
    while i >= 0:
        #Check if the number before is less than the one after and subtract
        if i < n-1 and roman_no[roman[i]] < roman_no[roman[i+1]]:
            output -= roman_no[roman[i]]
        else:
            output += roman_no[roman[i]]
        i-=1
    return output