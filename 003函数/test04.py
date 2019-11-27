#位置参数及默认参数

def power(x,n=2): #给定n默认参数为2
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
print(power(2,5))

#默认参数 学生注册函数
def enroll(name,gender,age=6,city='北京'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
print(enroll('jam','F',7))

#默认参数的坑
'''
def add_end(L=[]):
    L.append('END')
    return L
a = add_end([1,2,3])
print(a)
#以上会导致默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
'''
##修改：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#可变参数
'''
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
list = [1,2,3]
print(calc(list))
'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums = [1,2,3]
print(calc(1,2,3,5,7,9))
print(calc(1,2))
print(calc())
print(calc(nums[0],nums[1],nums[2]))
print(calc(*nums))

#关键字参数
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

extra = {'city':'beijing','job':'engineer'}
person('mik',29,**extra)
person('mik',29,city=extra['city'],job=extra['job'])

#递归函数
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))

#防止递归函数栈溢出
def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num-1,num*product)