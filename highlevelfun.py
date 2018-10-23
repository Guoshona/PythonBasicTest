# -*- coding:utf-8 -*-
'''
利用map()函数，把用户输入的不规范的英文名字，
变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，
输出：['Adam', 'Lisa', 'Bart']：
'''
list1 = ['adam','LISA','barT']
def mapChange (x):
	def changeLow(x):
		return x.lower()
	def changeCapitalize (x) :
		return x.capitalize()
list2 = list(map(mapChange,list1))	
print (list2)