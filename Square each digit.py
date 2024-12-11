#Welcome. In this kata, you are asked to square every digit of a number and concatenate them. 
#
#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
#
#Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
#
#Note: The function accepts an integer and returns an integer.
#
#Happy Coding!

def square_digits(num):
    # Your code here
        
        #Assign integer as a string
        s=str(num)
        
        #create list
        my_list=[]
        
        #for i in the range of the length of string taken from the integer
        for i in range(len(s)):
            
            #assign 2 squared of each term of the string to x
            x = (int(s[i]) ** 2)
            
            #Add each result to my_list
            my_list.append(x)
            
            #This converts each element in my_list to a string
            int_result = int(''.join(map(str, my_list)))
            
        print(int_result)
        return (int_result)
