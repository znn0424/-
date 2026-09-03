# import math
# math_values = math.sin(math.radians(30))
# print(math_values)
# a = -1
# b = -2
# c = 3
# d = (-b+(b**2-4*a*c)**(0.5))/(2*a)
# e = (-b-(b**2-4*a*c)**(0.5))/(2*a)
# f = (-b+math.sqrt((b**2-4*a*c)))/(2*a)
# print(d)
# print(e)
# print(f)
# #ctrl + /多行注释
# s = "hello world"
# print(len(s))
# print((s[0]))
# bool = True
# bool = False
# print(type(s))
#在控制台中可以直接测试代码用quit()或ctrl d退出
# usr_age = int(input("请输入你的年龄："))
# usr_age_after_10 = usr_age +10
# #注意整数类型不能和字符串一起输出
# print("10年后你"+str(usr_age_after_10)+"岁了")
# usr_height =float(input("请输入你的身高："))
# usr_weight =float(input("请输入你的体重："))
# usr_bmi =usr_weight/ (usr_height)**2
# print(usr_bmi )
# a = int(input ("请输入数字1："))
# b = int(input ("请输入数字2："))
# print(type(a))
# if (a>b) :
#     c=a
#     a=b
#     b=c
#     print(a)
#     print(b)
# else :
#     print(a)
#     print(b)
# #字典删除用del
# contacts ={("张伟",12):1234,("张伟",26):12345}
# print(contacts[("张伟",12)])
# wl_dict = {"kskbl":"康神开播了",
#             "zdjd":"真的假的",
#             "wkzkbl":"我靠真开播了"}
# # query = input("输入缩写：")
# # print(wl_dict[query])



# a = int(input("请输入数字，结束按0"))
# total = 0
# count = 0
# while a != 0:
#     count += 1
#     total += a
#     a = int(input("请输入数字，结束按0"))
# if count == 0:
#     print(0)
# else:
#     total_average = total / count
#     print(total_average)
#花括号内为可被替换的字符串
# name = input("请输入名字")
# year = input("请输入年份")
# print (f'''今年是{year}年
# 他的名字是{name}''')
# stu_dict = {("小明",18):1.123,("小红",19):2,("小光",20):2}
# for name,grade in stu_dict.items():
#      #print(f"{name}你好，你的成绩为{grade}")
#      print("{0}你好，你的成绩为{1:.2f}".format(name,grade))#保留两位小数

# def triangle_sector (a,b):
#     s =a*b/2
#     print(f"此三角形面积为：{s}")
#     return(s)
# s_1=triangle_sector(1,2)
# print(s_1)

#中位数

# 中位数函数
# def medium(num_list):
#     # 1. 对列表从小到大排序
#     sorted_list = sorted(num_list)
#     n = int(len(sorted_list))
#     if n % 2 == 1:
#         # 奇数：整数除法取中间下标
#         medium_num = sorted_list[n // 2]
#     else:
#         # 偶数：中间两个下标取平均
#         mid1 = sorted_list[n // 2 - 1]
#         mid2 = sorted_list[n // 2]
#         medium_num = (mid1 + mid2) / 2
#     # 返回结果，方便外部调用
#     print(medium_num)
#     return medium_num
#
# # 测试 [1,3,4,7,9] 排序后不变，长度5，中位数应为4
# medium([1, 3, 4, 7, 9])

# import statistics#ctrl+鼠标左键快速查看函数的使用方法，在pypi.org对第三方库搜索，在终端使用pip下载
# print(statistics.median([1,3,4,5,9]))

# class Panda_Trait:
#     def __init__(self, color,height,weight,age):
#         self.color = color
#         self.height = height
#         self.weight = weight
#         self.age = age
#     def speak(self):
#         print ("熊猫叫" * self.age)
#     def think(self,content):
#         print (f"熊猫思考{content}")
# panda_1 = Panda_Trait("黑白相间",180,60,5))
# panda_1.speak()
# panda_1.think("去爬树")
# print(f"熊猫的颜色是{panda_1.color}，它的身高为{panda_1.height}，它的体重为{panda_1.weight}")

# class Student:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#         self.grades = {"语文":0,"数学":0,"英语":0}
#
#     def get_grade(self,course,grades):
#         if course not in self.grades:
#             print("科目不存在")
#         else :
#             self.grades[course] = grades
#     def print_grades(self):
#         print(f"学生{self.name}的成绩是：{self.grades}")
#         for course in self.grades:
#             print (f"{course}：{self.grades[course]}分")
#
# chen = Student("小陈","123")
# li = Student("小李","12")
# print(chen.name)
# print(li.id)
# chen.get_grade("政治",92)
# print(chen.grades)
# chen.print_grades()

# class Employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#
#     def print_info (self):
#       print(f"该职工{self.name}和工号为{self.id}")
#
# class FullTimeEmployee(Employee):#不要忘记继承要写父类
#     def __init__(self, name, id,monthly_salary):
#       self.salary = monthly_salary
#       super().__init__(name,id)
#     def calculate_monthly_pay(self):
#         print(f"该员工{self.name}的月薪是{self.salary}")
#         return self.salary
#
# class PartTimeEmployee(Employee):
#     def __init__(self, name, id,daily_salary,work_days):
#       self.salary= daily_salary
#       self.work_days= work_days
#       super().__init__(name,id)
#     def calculate_monthly_pay(self):
#         total = self.salary*self.work_days
#         print(f"该员工{self.name}的月薪是{total}")
#         return self.salary*self.work_days
# chen = Employee("小陈",123)
# chen.print_info()
# zhangsan = FullTimeEmployee("张三",123,8000)
# lisi = PartTimeEmployee("李四",1234,250,20)
# zhangsan.calculate_monthly_pay()
# zhangsan.print_info()
# lisi.calculate_monthly_pay()

# f=open（“/usr/test/diary.txt","r") 打开文件,open之后要close /with open（“/usr/test/diary.txt","r") as f:

# with open("./data.txt","r",encoding ="utf-8") as f:
#     print(f.read())
# with open("./poem.txt","w",encoding="utf-8") as f:
#     f.write("我欲乘风归去\n又恐琼楼玉语")
# with open("./poem.txt","a",encoding="utf-8") as f:
#     f.write("\n高处不胜寒")
# try:
#     usr_weight = float(input("请输入你的体重:"))
#     usr_height = float(input("请输入你的身高:"))
#     usr_BMI = usr_weight/usr_height**2
# except ValueError:
#     print("你输入的值错误，请重新输入")
# except ZeroDivisionError:
#     print("禁止输入0，请重新输入")
# except:
#     print("未知错误")
# else :#不发生错误执行
#
# finally:#都执行
# def math_add(self,a,b):
# #     return a+b
# # from test_math import math_add
# # import unittest
# #
# # class Test_add(unittest.TestCase):
# #     def test_positive(self):
# #         self.assertEqual(math_add(1, 2), 3)
# #
# #     def test_negative(self):
# #         self.assertEqual(math_add(1, -2), -1)
# class ShoppingList:
#     def __init__(self,shopping_list):
#         self.shopping_list = shopping_list
#
#     def item_count(self):
#         return len(self.shopping_list)
#
#     def price_count(self):
#         total =0
#         for price in self.shopping_list.values():
#             total +=price
#         return total
#
# import unittest
# from unittest import TestCase
# from py_learning import ShoppingList
# class Test(unittest.TestCase):
#     def setUp(self):
#         self.shopping_list = ShoppingList({"英语书":10,"数学书":12})
#
#     def test_item_count(self):
#         self.assertEqual(self.shopping_list.item_count(), 2)
#
#     def test_price_count(self):
#         self.assertEqual(self.shopping_list.price_count(), 22)

# def num_squre(a):
#     return a**2
# def num_times_3(a):
#     return a**3
# def calculate_print(num,calculator):
#     result = calculator(num)
#     print(result)
# calculate_print(2,num_squre)
# (lambda num1, num2: num1 + num2)(2,3)


