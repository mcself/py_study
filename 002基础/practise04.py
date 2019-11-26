# -*- coding: utf-8 -*-
'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''
# BMI计算器，数据参考：百度百科

h1 = input('输入您的身高(米)：') #获取身高数据
w1 = input('输入您的体重（千克）：') #获取体重数据
h = float(h1) #数据类型转化
w = float(w1)
bmi = w/h**2 #计算公式
bmi1 = '%.2f' %bmi #格式化数字为保留两位
if bmi < 18.5:
    print('您的bmi指数为: ',bmi1,'偏瘦')
elif bmi < 23.9:
    print('您的bmi指数为: ',bmi1,'正常')
elif bmi >= 26.9:
    print('您的bmi指数为: ',bmi1,'偏胖')
elif bmi < 29.9:
    print('您的bmi指数为: ',bmi1,'肥胖')
else:
    print('您的bmi指数为: ',bmi1,'过度肥胖')


