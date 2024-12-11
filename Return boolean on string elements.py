#Return boolean on string elements
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
#Examples:
#solution('abc', 'bc') # returns true
#solution('abc', 'd') # returns false

def solution(text, ending):
    if ending in text and text[-1]==ending[-1]:
        return True
    else:
        return False
