def calculate_average_grade(grades_dict):
    # calculate the sum of all grades using sum()
    total = sum(grades_dict.values())
    #find the number of student by
    num_students = len(grades_dict)
    #calculate the average by dividing total by number of student
    avg = total / num_students
    #return the average grade 
    return avg
#example dictionary with student names as keys and their grades as values
student_grades = {"Alice": 85,"Bob": 90,"Charlie": 78,"David": 90,"Eva": 88} 
#call the function and print the averge grade
print("Average Grade:")