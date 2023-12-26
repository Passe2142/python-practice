student_scores = {
  "Harry": 61,
  "Ron": 93,
  "Hermione": 99, 
  "Draco": 84,
  "Neville": 77,
}


student_grades = {}


for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 80:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades) 
