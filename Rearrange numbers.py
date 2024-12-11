#Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
#Examples:
#Input: 42145 Output: 54421
#Input: 145263 Output: 654321
#Input: 123456789 Output: 987654321

def descending_order(num):

    # As a string is iterable (ie Each character in the string acts like an element in a sequence.), so simply use eg f = list(a)
    x=list(str(num)) #123456789 is the input and the output is: ['9', '8', '7', '6', '5', '4', '3', '2', '1']
    
    #Sorts the elements in list x in descending order (highest to lowest) rather than the default ascending order.
    x.sort(reverse=True)
    
    print (x) #['9', '8', '7', '6', '5', '4', '3', '2', '1']
    
    #combines all elements in the iterable x into a single string (using an empty string as the separator) and displays the result.
    print(''.join(x)) #987654321

   # combines all elements in the iterable x into a single string and converts that string into an    
      integer before returning it.    
      return (int(''.join(x))) 
