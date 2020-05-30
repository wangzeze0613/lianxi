#类型
"""
print("hello word!```````")  #字符串 str
print(100)  #整数  int 
print(1.023)  #小数 float 
print(True)   #布尔值 bool 
print(False)  #布尔值 bool 
print(None)   #空 nonetype
print(())    #元祖 tuple
print([])   #数组 list
print({})   #字典 dict
len()    #获取长度
print("我是最棒的")

print("王泽泽"+"七七")
print("三流之路"*5)

#画房子
print("        a       ")
print("      a   a     ")
print("     aaaaaaa    ")
print("     a     a    ")
print("     a     a    ")
print("     a     a    ")
"""
#type()   查看类型
"""
1、任何数据都可以转换成字符串
2、字符串转换成数字需要满足长的像这个规律
3、字符串可以转换成元组、数组
"""
#input用法
"""
a=input()
b=input()
print(len(a) + len(b))
"""

#print("查看类型",type()
#元组 tuple
"""
a=(1,2,3,4,5,6,True,False)  #元组
b=(6,7,8,9,a)      #二维元组
print(a.count(5))  #统计元组中5的数量
print(a.index(6))  #获取6字符在元组中的下标
#b=int(input())    #输入元组下标
#print(a[b])       #输出指定元组中的字符
"""



#数组  list 列表
"""
aa=["a","b","c","我","爱你",1,2,"c"]
print(aa.count("c"))  #统计数组中c的数量
print(aa.index("c"))  #获取第一个c字符在数组中的下标
"""

#元组和数组的区别：元组不可修改，数组可以修改
"""
aa.append("d")    #往数组中，追加数据
aa.insert(3,"d")  #在数组的指定位置，插入数据
aa.remove("c")    #删除数组中的第一个"c"
c=aa.pop(3)       #把下标为3的值，取出来
aa.append(c)
aa.reverse()      #把数组颠倒过来
aa[1]="q"         #把下标为1的值修改为q
bb=[1,2,3]
cc=[4,5,6]
bb.sort()           #把数组中的值排序
bb.extend([6,7,8])  #把数组合并并追加到尾巴上
cc.clear()         #把数组清空

print(aa) 
print(bb)
print(cc)
"""
#练习
"""
a=input()
b=input()
cc=[len(a),len(b)]
cc.sort()
print(len(a)+len(b))
print(cc)
"""


#字典  键值对  key:value   没有下标
"""
a={
   "name":"wangzeze",
   "sex":"男",
   "age":"23"
}
print(a["age"])
a["adc"]="女枪"
#a.update(key：value)     #如果key存在，修改其值，如果不存在，则添加其key：value
a.get("name")            #如果key不存在，那么返回空
a["name"]                #如果key不存在，那么报错！
#a.pop()                 #取值
#a.clear()               #清空
#a.keys()                #展示a字典的所有key    可以用数组展示  list(a.keys())
#a.values()              #展示a字典所有的值
print(a)
"""
#判断
"""
a=input()
b=input()
if a> b :
    print("a大于b")
elif a==b:
    print("a=b")
else:
    print("a小于b")
"""


"""
age=int(input("请输入你的年龄："))
if age>65:
    print("你退休了")
elif age>40:
    print("你年纪大了，注意身体")
elif age>25:
    print("你年轻气盛")
elif age>18:
    print("你年轻的很")
else:
    print("你未成年")
"""
"""
zhanghao=input()
mima=input()
a=len(zhanghao)
b=len(mima)

if a>5 and b<12:
    if b>8 and b<16:
        c={"zhanghao":zhanghao,"mima":mima}
        #c["zhanghao"]="mima"
        print(c)
        print("yes")
    else:
        print("no")
else:
    print("0")
"""
# while
"""
a=20
while a>0:
    print("好",a)
    a=a-1
"""

"""
xx = [1,2,3,4,"哈哈","嘿嘿","回锅肉","小龙虾","回锅肉"]
a=1
while a<len(xx):
    print((xx[a]))
    a=a+2
"""

# for in  遍历
"""
xx = [1,2,3,4,"哈哈","嘿嘿","回锅肉","小龙虾","回锅肉"]
for i in range(1,len(xx),2):
    print(xx[i])
"""   
  
#for i in range(1,99,2):     #(起始值，终点值，步进值)
"""
xx = [1,2,3,4,"哈哈","嘿嘿","回锅肉","小龙虾","回锅肉"]
a=1
for i in xx:
    if a<len(xx):
        print(xx[a])
        a=a+2
"""
#用for循环打印九九乘法表

"""
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,end=" ")
    print()
 """  

"""
练习：
现在有10个学生的成绩，需要录入到系统中。
这是个人分别是，张三、李四、王麻子、浪晋、流云、希希、小梁、二狗、陈平安、朱珠、亚索
并且名字和成绩需要对应上。
而且大于60的和小于60的需要分开存放。
"""
"""
name=["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
#a=0
good={}
bad={}
#while a<10:
  #  a=a+1
   # name=input("请输入名字：")
for i in name:
    grad=float(input("请输入分数："))
    if grad>60:
        good[i]=grad
    else:
        bad[i]=grad
print("大于60分的同学：",good)
print("小于等于60分的同学：",bad)
"""





"""
#通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次
light={"红灯":30,"绿灯":35,"黄灯":3}
for i in light:
    for j in range(light[i]):
        print(i,"倒计时还剩下",light[i]-j,"秒")

"""



#既包含又相等
#项目--包--模块--类--方法--变量
"""
name=["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
for i in name:
    if i=="浪晋":
        continue
    if i=="二狗":
        print(name.index("二狗"))  #获取数组中第一个二狗的下标
        break
    print(i)
"""


"""
import func
func.chengfa(5,6)

from func import chengfa
chengfa(6,7)
"""


"""
#pip list  #查看已经安装的第三方的包
pip install #安装第三方包
pip uninstall #卸载安装的包

pymysql   #操作mysql数据库的
selenium   #
requests   #
xlrd        #

"""   



"""
print("hello word")


"""
































