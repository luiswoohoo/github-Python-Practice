# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}


# Print the name and grade percentage of the student with the highest total of points.
def highest_grade_and_student(student_grades_dict):
    max_grade = 0
    max_student = ''
    for student, grades in student_grades_dict.items():
        # print(sum(grade))
        if sum(grades) > max_grade:
            max_grade = sum(grades)
            max_student = student
    return max_grade, max_student


highest_grade = highest_grade_and_student(student_grades)[0]
highest_student = highest_grade_and_student(student_grades)[1]
grade_percentage = (highest_grade / 500) * 100

print('The student with the highest point total is {} with {}%'.format(highest_student, grade_percentage))
print()

# Find the average score of each assignment.
grades_list = list(student_grades.values())
num_assignments = len(grades_list[0])
num_students = len(grades_list)

for i in range(num_assignments):
    total_points = 0
    for j in range(num_students):
        total_points += grades_list[j][i]
    print('Average for assignment {} is {}'.format(i + 1, total_points / num_students))
print()

# Find and apply a curve to each student's total score, such that the best student has 100% of the total points.
print('Grades on a curve')
for student, grades in student_grades.items():
    print('{}: {:.0f}'.format(student, (sum(grades)/highest_grade * 100)))


