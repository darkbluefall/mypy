#author : 青与白
#description : 猜数字小游戏

from random import randint
# import pymysql
import time


num=randint(1,99)
t=0
numget=0
big=['亲，你输的数字大了哟','万水千山总是情，输个小点的行不行','输个精致点的好伐','要不咱们数个小点的试试？','给老子听好，输个小点的']
small=['亲，你输的数字小了哟','万水千山总是情，输个大点的行不行','输个粗犷点的好伐','要不咱们数个大点的试试？','给老子听好，输个大点的']

print("**********正在初始化游戏**********")
time.sleep(2)
print("**********正在进入游戏**********")
time.sleep(2)
print("**********游戏即将开始**********")
time.sleep(2)
print("**********请开始你的表演**********")


while numget!=num:
	n=input('请输入数字:')
	numget=int(n)
	t=t+1
	print("**********比对结果中**********")
	time.sleep(3)
	if numget>num:
		print(big[randint(0,4)])
	elif numget<num:
		print(small[randint(0,4)])

print ('恭喜你猜对了,一共猜了%d次'%t)

# mycon=pymysql.Connect(host='localhost',port=3306,user='root',passwd='123456',db='qingyuby')
# mycursor=mycon.cursor()
# name = input('请输入你的大名：')
#
# mycursor.execute('insert into num values (%r,%d);'%(name,t))
# mycon.commit()
# mycursor.execute('select * from num order by times limit 3')
# paihang=mycursor.fetchall()
# list=['第一名','第二名','第三名']
# print('前三名分别是')
# for i in range(3):
# 	print('%s,%s,猜测次数为%d'%(list[i],paihang[i][0],paihang[i][1]))