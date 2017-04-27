#!/usr/bin/env python
this_year =2016
while True:
	name = raw_input("please input your name:").strip()
	if len(name != 0)
		break

age = int(raw_input("how old are you?"))
sex = raw_input("please input your sex:")
dep = raw_input("which department:")
message = '''Information of the company staff:
	Name:%s
	Age :%d
	Sex :%s
	Dep :%s
	''' % (name, age, sex, dep)
print message
if age < 28:
	print "Congratulations! your've got half day's public holiday!"
else:
	print "Sorry,you are too old to have this holiday! get back to work!"


	
