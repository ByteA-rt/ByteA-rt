#An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
#Example: (Input --> Output)
#"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

def is_isogram(string):
    string = string.lower()
    if len(string) <=1:
        print ("a", True)
        return True
    elif len(string) > 1:
        #Checks for if next letter is the next letter in the alphabet
        for i in range(len(string)-1):
            if string[i] > string[i+1]:
                print (string[i])
                print ("b", False)
                return False
                
        #Checks for number of characters in a string
        for char in string:
            if string.count(char) > 1:
                print("c", False)
                return False
    
    print("c", True)
    return True
