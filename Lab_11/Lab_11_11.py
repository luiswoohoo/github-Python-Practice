import csv


def convert_tsv_to_list(file):
    with open(file, 'r') as tsv_file:
        content = csv.reader(tsv_file, delimiter='\t')
        return list(content)


def determine_letter_grades(student_data):
    for data in student_data:
        num_grade = (int(data[2]) + int(data[3]) + int(data[4])) / 3
        if num_grade >= 90:
            letter_grade = 'A'
        elif 80 <= num_grade < 90:
            letter_grade = 'B'
        elif 70 <= num_grade < 80:
            letter_grade = 'C'
        elif 60 <= num_grade < 70:
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        data.append(letter_grade)


def calculate_exam_averages(student_data):
    midterm1 = 0
    midterm2 = 0
    final = 0
    students = len(student_data)
    for data in student_data:
        midterm1 += int(data[2])
        midterm2 += int(data[3])
        final += int(data[4])
    exam_averages = [midterm1 / students, midterm2 / students, final / students]
    return exam_averages


def write_report(student_data, averages):
    with open('report.txt', 'w') as f:
        for data in student_data:
            output_string = ''
            for i in data:
                if data[len(data) - 1] == i:
                    output_string += i
                else:
                    output_string += (i + '\t')
            f.write(output_string + '\n')
        f.write('\nAverages: midterm1 {:.2f}, midterm2 {:.2f}, final {:.2f}\n'
                .format(averages[0], averages[1], averages[2]))


input_file = input()

new_list = convert_tsv_to_list(input_file)

# print(new_list)

determine_letter_grades(new_list)

# print(new_list)

averages = calculate_exam_averages(new_list)

write_report(new_list, averages)
