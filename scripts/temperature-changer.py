def change():
  f = float(input('请输入华氏度: '))
  c = (f - 32) / 1.8
  print(f'{f:.1f} 华氏度转为换摄氏度为 {c:.1f}℃')

change()
