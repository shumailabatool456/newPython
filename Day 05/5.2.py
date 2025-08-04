student_heights = input("Enter a list of student heights").split()

for n in range(0, len(student_heights)):

 student_heights[n] = int(student_heights[n])
print(student_heights)  
total_height = 0
for height in student_heights:
 total_height  += height
 no_of_students = len(student_heights)
print(total_height)
avg = round(total_height/no_of_students)
print(avg)



