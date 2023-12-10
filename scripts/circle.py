import math


def circle():
  radius = float(input('please input radius: '))
  perimeter = 2 * math.pi * radius
  area = math.pi * radius * radius
  print(f'the perimeter of circle is {perimeter:.2f}')
  print(f'the area of circle is: {area:.2f}')

circle()
