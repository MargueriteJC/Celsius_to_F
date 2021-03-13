#此程序涉及数据类型data type的转换
centegrade = input('Please input todays centegrades in Celsius: ') # Input的结果是string
centegrade = int(centegrade) #把string转化成int
print(centegrade, '`C') 
f = centegrade * 9 / 5 + 32 #string不能用于数学计算
print('Equal to', f, '`F')