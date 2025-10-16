#define a funtions to process the list and count iteration
def getMYList():
    #crate a list of number 
    list=[10,20,30,40,50,60]
    #initialize a counter varible
    count = 0
    #loop through each numberin the list 
    for num in list:
        print(num)
        count += 1
    #return the total number of iterations
    return count
#call the function and store the result
total = getMYList() 
#print the total number of iterations
print(total)