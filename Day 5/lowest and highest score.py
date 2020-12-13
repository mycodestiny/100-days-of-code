#lowest and highest score.py



student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

highest_score = 0
low_score = 100

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)

for score in student_scores:
    if score < low_score:
        low_score = score
print(low_score)


# easy

print(max(student_scores))
print(min(student_scores))
