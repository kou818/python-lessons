students = ['Mary','John','Kevin']

num = len(students)

#for i in range(len(students)):
# print('students = ['+"'"+students[i]+", '"+students[i]+", '"+students[i]+"']")

for i in range(len(students)):
	print(students[i:]+students[:i]+students[:0])
