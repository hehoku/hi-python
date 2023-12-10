def isLeap():
  year = int(input('please enter year: '))
  isLeap = False
  if (year % 4 == 0 and year % 100 != 0):
    isLeap = True
  if (year % 400 == 0):
    isLeap = True

  if (isLeap == True):
    print(f'{year} is leap year')
  else:
    print(f'{year} is not leap year')

isLeap()
