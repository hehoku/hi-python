score = float(input('please enter your score:'))

if score >= 90:
  grade = 'A'
elif score >=80:
  grade = 'B'
elif score >=70:
  grade = 'C'
elif score >=60:
  grade = 'D'
else:
  grade = 'E'

print(f'your grade is {grade}')
