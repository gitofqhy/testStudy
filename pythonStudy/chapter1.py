#print语句
print("hello world")
print("你好")
print("(@^_^@)")

#字符串
print("hello "+"华盈")
print("hello 'huaying'")

#变量
today_date = "2018/9/25"
a_char = 'a'
a_string = "I like Python !"
a_num = 1
a_float = 1.0
a_bool = True
list1 = ['python', 'c', 'c++', 1997, 2000] #列表
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c"]
tup1 = ('python', 'c', 'c++', 1997, 2000)#元组
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c"
dict1 = {'Alice': '2341', 'Bath': '9102'}#字典

#数学运算
product = 2 * 3
2398 % 11
3 ** 5
print(2 ** 3)

#变量更新
the_price_of_book1 = 30
the_price_of_book1 *= 0.8
the_price_of_book2 = 45
the_price_of_book2 *= 0.6
fare = 10
total = the_price_of_book1 + the_price_of_book2 + fare
print(total)

#注释
#单行注释
'''
多行注释
多行注释
'''

#数字
pen = 2
price = 4.25
total_cost = pen * price
print(total_cost)
print(type(total_cost))

#多行字符串
haiku = """
The old pond,
A frog jumps in:
Plop!"""
print(haiku)

#布尔值
a = True
b = False
print(2 == a)
print(2 == b)

#类型转换
number_1 = 7
str_1 = str(number_1)
number_2 = int(str_1)
print(int(4.5))

float_1 = 0.25
float_2 = 40.0
product = float_1 * float_2
print(product)

big_string = "The product was X"
big_string = "The product was " + str(product)
big_string = "I have {} dogs at home!".format(str(18))
print(big_string)

#复习
skill_completed = "Python Syntax"
case_study = 13
points_per_case = 5 #每个小节的分值
point_total = 100
point_total += case_study * points_per_case
print("I got {} points!".format(str(point_total)))

time1 = 32 + 6 * 1 + 3 * 0.5 + 6 * 2
print("跑完时间6点{}分".format(str(time1)))





