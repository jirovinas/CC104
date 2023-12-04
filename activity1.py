student_data = [
    ["Alice", [85,90, 92], ["Math", "English", "Science"]],
    ["Bob", [78, 88, 80], ["Math", "English", "Science"]],
    ["Charlie", [92, 94, 89], ["Math", "English", "Science"]],
    ["David", [80, 85, 88], ["Math", "English", "Science"]],
]

#1. 
print("Number 1: ")
for every_scores in student_data:   
    name = every_scores[0]
    score = every_scores[1]
    average = sum(score) / len(score)
    rounded_average = round(average, 2)
    print(f"{name} = {rounded_average}")
print("\n")


#2. 
print("Number 2: ")
highest_average = 0
highest_name = ''
for every_scores in student_data:
    current_name = every_scores[0]
    score = every_scores[1]
    average = sum(score) / len(score)
    rounded_average = round(average, 2)

    if average > highest_average:
        highest_average = rounded_average
        highest_name = current_name
print(f"The student with the highest average score is {highest_name} with the average of {highest_average}.")

print("\n")

#3. 
new = [["Eva", [95, 91,88], ["Math", "English", "Science"]]]
student_data.extend(new)

#4.
print("Number 3 and 4: ")
print(student_data)
print("\n")
#5.
print("Number 5: ")
lowest_average = 0
lowest_name = ''

for every_scores in student_data:
    current_name = every_scores[0]
    score = every_scores[1]
    average = sum(score) / len(score)
    rounded_average = round(average, 2)



    if average < lowest_average:
        lowest_average = average
        lowest_name = current_name
        student_data.remove(every_scores)

    elif lowest_average == 0:
        lowest_average = average
        lowest_name = current_name
print(f"The student with the lowest average score is {lowest_name} with the average of {lowest_average}.\n\n\n")

#6. 
print("Number 6: ")
print(student_data)
print("\n")


#7. 
print("Number 7 and 8: ")
english_scores = []

for every_data in student_data:
    scores = every_data[1]
    subjects = every_data[2]
    english_index = subjects.index("English")
    english_score = scores[english_index]
    english_scores.append(english_score)

#8.
print(english_scores)
print("\n")

#9. 
print("Number 9 and 10: ")
math_scores = []
for every_data in student_data:
    scores = every_data[1]
    subjects = every_data[2]
    math_index = subjects.index("Math")
    math_score = scores[math_index]
    math_scores.append(math_score)

math_scores.sort(reverse=True)
#10.
print(f"The descending order : {math_scores}")
print("\n")

#11. 
print("Number 11: ")
math_list = []
english_list = []
science_list = []
highest_average = 0
highest_subject = ""
for every_score in student_data:
    scores = every_score[1]
    subjects = every_score[2]
    math_index = subjects.index("Math")
    math_score = scores[math_index]
    math_list.append(math_score)

    english_index = subjects.index("English")
    english_score = scores[english_index]
    english_list.append(english_score)

    science_index = subjects.index("Science")
    science_score = scores[science_index]
    science_list.append(science_score)

math_average = sum(math_list) / len(math_list)
print(f"Math Average: {math_average}")
english_average = sum(english_list) / len(english_list)
print(f"English Average: {english_average}")
science_average = sum(science_list) / len(science_list)
print(f"Science Average: {science_average}")
print("\n")

#12. 
print("Number 12: ")
print(f"The subject with the highest average score is English with the average of {english_average}\n\n\n")


#13. 
student_data[1][1] = [85, 87, 90]

#14. 
print("Number 13 and 14: ")
print(student_data[1])
print("\n")

#15. 
print("Number 15: ")
for every_scores in student_data:
    name = every_scores[0]
    score = every_scores[1]
    average = sum(score) / len(score)
    rounded_average = round(average, 2)
    print(f"{name} = {rounded_average}")
print("\n")

#16. 
print("Number 16: ")
for every_scores in student_data:
    name = every_scores[0]
    score = every_scores[1]
    if 100 in score:
        print(f"{name} has a perfect score")
        break
    else:
        print("None has a perfect score")
        break

