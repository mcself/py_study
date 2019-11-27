#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解。
计算平方根可以调用math.sqrt()函数：
import math
math.sqrt(2)
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
'''

'''
import math
def quadratic(a, b, c):
    if b**2-4*a*c < 0:
       return'该方程无解'
    elif b**2-4*a*c == 0:
        x = -b/(2*a)        #print('该方程只有一个解，该解为%-6.1f'%x)
        return x
    else:
        x = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        y = (-b-math.sqrt(b**2-4*a*c))/(2*a)    #print('该方程有两个解，分别为%-6.1f和%-6.1f' %(x,y))
        return x,y   # 第一个"%"后面的内容为显示的格式说明，6为显示宽度，3为小数点位数，f为浮点数类型

'''
import math
def quadratic(a,b,c):
    if b**2-4*a*c < 0:
        return '方程无解'
    elif b**2-4*a*c == 0:
        x = -b/(2*a)
        return  '方程解为：%6.3f'%x
    else:
        x = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        y = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x,y #'方程的两解：\nx为：%6.1f,y为：%6.1f'%(x,y)

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
