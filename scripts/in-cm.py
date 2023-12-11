value = float(input('please input value:'))
unit = input('please input unit:')

if unit == 'in' or unit == '英寸':
  print(f'{value} 英寸为 {(value * 2.54):.2f} 厘米')
elif unit == 'cm' or unit == '厘米':
  print(f'{value} 厘米为 {(value / 2.54):.2f} 厘米')
else:
  print('please input in or cm')
