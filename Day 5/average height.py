#this calculates average of list of heights.

#easy

student_heights = [180, 124, 165, 173, 189, 169, 146]
total_height = sum(student_heights)
total_students = len(student_heights)
print(round(total_height / total_students, 3))


#hard

total = 0
sum_height = 0
students = 0

main_list = [180, 124, 165, 173, 189, 169, 146]
for numbers in main_list:
    sum_height += numbers
for numbers in main_list:
    students += 1
print('total_height: ', sum_height)
print('total students: ', students)
total = round((sum_height / students),2)
print('total height average is: ', total, "cm")

