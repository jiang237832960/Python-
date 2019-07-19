# 第一种：直接使用+号拼接，无法拼接数字类型
a = '欢迎'
# Traceback (most recent call last):
# File "c:\Users\234832960\Desktop\Python-demo\格式化字符串的四种方式.py", line 3, in <module>
# print(a+123)   
# TypeError: can only concatenate str (not "int") to str
print(a+'你好')

# 第2种：print(a,b)传入两个参数，会依次打印输出
b = 123.9
print('wo111 ',b)

# 第3种：使用占位符，常用的有三种：
# %s：string类型，也可拼接数字类型，但是无法控制小数点位数
# %f：float类型，可以控制小数点位数，自动四舍五入
# %d：整数类型，直接舍去小数点之后的数据
c = '我是谁%3.5s'%123456# %3.5s中3.5表示最少三个位置，最多五个
c = '我是谁%.2f'%1234.456# %0.2f中小数点之后最多2位，缺点是无法控制整数位
c = '我是谁%.2d'%1234.456# 缺点是无法控制整数位
print(c)

# 第4种：pyhton3.x中的新特性，格式化字符串 可以直接在字符串之中写入变量
d = f'我是谁{a}{c}'
print(type(b))# type()函数用于检测变量类型，结果作为返回值，需用变量来接收。