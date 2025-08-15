student_scores = {
                  "Umama": 78, 
                  "Hania": 88, 
                  "Hala": 76, 
                  "Zaly": 99, 
                  "Aira": 65,
                  }
student_grades ={}
for student in student_scores:
    score = student_scores[student]
    if score >90:
       student_grades[student]= "Outstanding"
    elif score > 80:
         student_grades[student]= "Exceeds Expectation"
    elif score > 70:
         student_grades[student]= "Acceptable"
    else: 
         student_grades[student]= "Fail"

print(student_grades)