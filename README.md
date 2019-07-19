# Python-基础

## Python的介绍
    python是一门解释型语言，属于通用型编程语言。
	python由荷兰程序员吉多·范罗苏姆创造，第一版发布于1991年，可以看成是一种改良（加入了一些其他编程语言的优点，例如面向对象）的LISP。
	作为一种解释型语言，python的设计哲学强调代码的可读性与简洁的语法，尤其使用空格缩进来控制代码段而非使用大括号或关键字来控制，
	相较于java或者C语言，python能让开发者以更少的代码实现功能。
```
life is short,you need python.
人生苦短,你需要python。
```
## Python的用途
	- WEB应用（如Facebook，豆瓣等）
	- 爬虫程序
	- 科学计算
	- 自动化运维
	- 大数据（数据清洗）
	- 云计算
	- 人工智能
	- 桌面应用与游戏 

## Python解释器
	python的解释器有四种：
	1.CPython：官方解释器。
	2.PyPy：python语言写的解释器。
	3.Iron Python：.net语言写的解释器。
	4.JPython：Java语言写的解释器。

## Python的基本概念
	1.表达式
		表达式类似于数学公式
		例如：1+2  3*4
		表达式会产生一个结果，但是不会对程序产生实质性的影响
		在交互模式中执行，解释器会自动输出结果
	2.语句
		语句指在程序中完成某个功能的句子，如打印信息、变量赋值等
		例如：print(a)   a = '哈哈'
		语句的执行会对程序产生一定的影响
		在交互模式中，解释器不一定会输出结果
	3.程序（program）
		程序就是由一条一条语句和一条一条的表达式组成的一个集合
	4.函数（function）
		函数是一种语句，用于完成某些特定的功能
		函数的形式：xxx()
		函数的分类：
			内置函数：由python提供的函数，可直接使用
			自定义函数：由编程人员自行定义的函数
		函数的两个要素：
			参数：
				- ()中的内容就是参数
				- 函数的参数可以没有，也可以是多个，参数直接使用,进行分割
			返回值：
				- 返回值就是函数执行的返回结果

## Python的基本语法
	1.python中严格区分大小写，ab与Ab是两个不同的属性
	2.python中每一行就是一条语句，以换行作为结束
	3.python中的每条语句都不要过长，规范建议为不超过80个字符
	4.一条语句可以分多行编写，每行以\结尾
	5.python是缩进严格的语言，所以在python中不要随便使用缩进
	6.python中使用#来编写注释，多行注释就每行开头写上#
