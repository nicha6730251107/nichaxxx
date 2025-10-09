"""
Create a grade processing system with the following requirements:

A global variable passing_grade = 50

(1) A function input_students(num_students) that:

- Creates and returns a list of dictionaries
- Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

(2) A function calculate_averages(students) that:

- Uses nested loops to calculate each student's average
- Adds an 'average' key to each student dictionary
- Modifies the original list (demonstrate list mutability)

(3) A function display_results(students) that:

- Loops through students
- Uses the global passing_grade to determine pass/fail
- Prints each student's name, average, and status (PASS/FAIL)
"""

passing_grade = 50

def input_students(num_stuudents=0):
    students = [
        {
            'name': 'Boonchoo'
            'scores': [45,52,63]
        },
        {
            'name': 'Steve'
            'scores': [87,75,68]   
        }
    ]
    return students 

def calculate_average(students):
    for student in students:
        sum = 0
        for score in student['scores']:
            sum = sum + score
            student['average'] = sum / len9(student['scores'])

def display_results(students):
    for student in students:
        print("Student Name:%s" % (student['name']))
        print("Student Average Score: %.2f" % (student['average']))
        if student['average'] >= passing_grade:
            print("Student Stauts: PASS")
        else:
            print("Student Status: FALL")
    
students = input_students()
students = caculate_average(students)
display_results(students)