#Reverse array of numbers
# Convert number to reversed array of digits
#Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#Example(Input => Output):
#35231 => [1,3,2,5,3]
#0 => [0]

def digitize(n):
    # Shows the value of n
    print ("The input string is", n)
    
    # Stores the length of the string version of n
    max_length = (len(str(n)))
    print ("the length of the integers converted to string is", max_length)
    
    #Creates an empty list
    result = []
    print("The empty list is", result)
    
    # String version of the integer n
    n_str=str(n)
    print ("The list of the string is", n_str)
    
    #Location of string at index 0
    print ("The location at 0 in the list is", n_str[0])
    
    #Populates list with n 
    for i in n_str:
        result.append(i)
    print("For i  that is the loop variable that takes on each value in n during each iteration and n must be iterable: For this loop to work, n must be an iterable object (e.g., list, string, tuple, dictionary, or any custom iterable")
    print(result)
    
    # Stores the number in reverse order without any sorting
    resorted_result = []
    for i in result:
        resorted_result = str(n)[::-1]
    print ("the number in reverse without resorting", resorted_result)
    
    #Converts the string list to integer list
    integer_results = []
    for i in resorted_result:
        integer_results.append(int(i))
    print("The integer version of the array is", integer_results)
   return (integer_results)
