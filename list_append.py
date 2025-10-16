#define a fuctio that append a vlue to a given list S
def  append_to _list(value, 1st):
    #use the .append () method to add the value to list 
    1st.append(value)

#create an empty list to store use input
my_list =[]

#start a loop to keep asking the user for values to append
while True:
    #prompt the user to enter a value 
    value = input("enter an initial value: ")
    #Append the entered value to the list using the functiom
    append_to_list(value, my_list)
    #ask the user if they want to continue adding more values
    cont = input("would you like to enter another value to append to the list? (yes or no): ")
    #if the user enter 'no' end the loop
    if cont.lower() == 'no':
        break
#after end the loop print the list 
print(my_list)