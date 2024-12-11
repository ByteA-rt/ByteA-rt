#Return middle string
# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.
#If the string's length is odd, return the middle character.
#	If the string's length is even, return the middle 2 characters.
#Examples:
#"test" --> "es"
#"testing" --> "t"
#"middle" --> "dd"
#"A" --> "A"

def get_middle(s):
    length = int(len(s))
    middle  = int(length // 2)
    if length == 1:
        return (s)
    elif length % 2 == 0:
        first_middle = (middle - 1)
        second_middle = (middle + 1)
        return (s[first_middle: second_middle])   
    elif length % 2 > 0:
        return (s[middle])  
    else:
        return None
