num_grades = int(input("How many grades do you want to enter(max 10): "))
if num_grades > 10:
    num_grades = 10

count = 0 
while count < num_grades:
    grade = int(input(f"Enter grade #{count + 1}: "))
    print(f"Grade entered: {grade}")
    count += 1
    
    print(f"the user has entered {num_grades} grades and is now done")