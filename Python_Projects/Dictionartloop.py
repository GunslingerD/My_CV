student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {
    
}

for n in student_scores:
    if student_scores[n] >=91:
        student_grades[n]="Outstanding"
    elif student_scores[n] >81:
        student_grades[n]="Exceeds Expectations"
    elif student_scores[n] >71:
        student_grades[n]="Acceptable"
    elif student_scores[n] <=70:
        student_grades[n]="Fail"

print(student_grades)