#define a fumction that slices the stringform position 0 to 3
def slice_my_string(s):
    #Return the substring form index 0 up to but not including index 4
    return s[0:4]

#pompt the user to enter a string 
user_input = input ("enter a string:")
 
 #call the fuction with the user input and store the result
 result = slice_my_string(user_input)

 #print the sliced string to the console 
 print(result)
