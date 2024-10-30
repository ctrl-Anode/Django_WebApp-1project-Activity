students_scores = [('John', 85), ('Maria', 92), ('Tom', 76), ('Sarah', 90)]
highest_score = 0
highest_student = None
for student, score in students_scores:
    if score > highest_score:
        highest_score = score
        highest_student = student
print(highest_student)