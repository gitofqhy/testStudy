# 条件分支
def choice():
    print("请选择，左还是右？")
    answer = input("输入 左 或者 右: ")
    if answer == "左" or answer == "左边":
        print("你选择了左")
    elif answer == "右" or answer == "右边":
        print("你选择了右")
    else:
        print("你两个都没选，你决定再试一次")
        choice()

# choice()

# 判断多个条件
print(False and False)
print(-(-(-(-2))) == -2 and 4 >= 16 ** 0.5)
print(19 % 4 != 300 / 10 / 10 and False)
print(-(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2)
print(True and True)
print(2 ** 3 == 108 % 100 or "cleese" == "King Artthur")
print(True or False)
print(100 ** 0.5 >= 50 or False)
print(True or True)
print(1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1)
print(not True)
print(not 3 ** 4 < 4 ** 3)
print(not 10 % 3 <= 10 % 2)
print(not 3 ** 2 + 4 ** 2 != 5 ** 2)
print(not not False)
'''
布尔操作符的优先级
1.not最优先
2.and第二
3.or最后
'''
print(True or not False and False)  # 结果为True
print(True or ((not False) and False))

def grade_converter(grade):
    if grade >= 90 and grade <= 100:
        return "优秀"
    elif grade >=80 and grade <= 89:
        return "良好"
    elif grade >= 70 and grade <= 79:
        return "尚可"
    elif grade >= 60 and grade <= 69:
        return "待改进"
    else:
        return "不及格"

print(grade_converter(90))
print(grade_converter(70))
print(grade_converter(50))

