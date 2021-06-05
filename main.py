# Yi Xin Tan
# 21May2021
# Applied Computing Practice SAC

# get number of students
num_of_students = int(input('Please enter a number of students: '))

# create empty list to store student scores
student_scores = []

# loop through to get score of each student
for s in range(1, num_of_students+1):
    score = float(input(f'Please enter score for Student{s}: '))  # get user input
    student_scores.append(score)  # append user input to student_scores list

# calculations for lowest, highest and average score
lowest_score = min(student_scores)
highest_score = max(student_scores)
average_score = sum(student_scores)/len(student_scores)

# round average score
average_score = round(average_score, 2)

# prints lowest, highest and average scores
print(f'Lowest Score: {lowest_score}')
print(f'Highest Score: {highest_score}')
print(f'Average Score: {average_score}')
