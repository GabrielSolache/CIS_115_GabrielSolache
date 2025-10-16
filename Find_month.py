#define a function that searches for a month in the months list
def search(month):
    #create a list of months
    months =["january","february,'march","april","may","june","july","august","september","october","november","december"]
    #check if the month is in the list
    if month in months:
        #if  found, print a success message using an f-string
        print(f"we found {month} in the months list")
    else:
        #if not found, print a failure message using an f-string
        print(f"{month} is not found in the months list")
        #prompt the user to enter a valid month
        month = input("please enter a month to search: ")
        #call the search function with the user input
        search(month)