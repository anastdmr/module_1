grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
students = sorted(students)
#print (students)
dict_sr_ball = {}
for i in range(5):
    ball = 0
    for j in range (len(grades[i])):
        ball = ball + grades[i][j]
    sr_ball = ball/len(grades[i])
    dict_sr_ball.update({students[i]:sr_ball})
    sr_ball = 0.0
print (dict_sr_ball)