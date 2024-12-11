#Convert String to arrays
# Write a function to split a string and convert it into an array of words.
#Examples (Input ==> Output):
#"Robin Singh" ==> ["Robin", "Singh"]
#"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favor

def string_to_array(s):
    if s=="":
        return [""]
    return s.split()  
    
print(string_to_array(s))  # Output: ['1', '2', '3']
