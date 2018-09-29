# 8.10While循环
# 任务1
count = 0
for i in range(0, 10):
    if count <= 9:
        print("现在执行if语句，count =", count)
        count += 1


# 8.20 循环进入条件
# 任务1
loop_condition = True
while loop_condition:
    print("我是循环体里的语句")
    loop_condition = False

# 任务2
num = 1
while num <= 10:
    print(num ** 2)
    num += 1

# 8.30 用while处理用户输入
# 任务1
choice = input('喜欢这个课程吗（y/n）')
while choice != 'y' or choice == 'n':
    choice = input("对不起，无法识别输入值，请重新输入（y/n）：")

# 8.40死循环
# 任务1
count = 0
while count < 10:
    print(count)
    count += 1

# 8.50用break结束循环
# 任务1
count = 0
while True:
    print(count)
    count += 1
    if count >= 10:
        break

count = 0
while True:
    count += 1
    if count == 6:
        continue
    print(count)
    if count >= 10:
        break


# 8.60 for循环
# 任务1
for i in range(0, 20):
    print(i)

# 任务2
thing = "spam!"
for c in thing:
    print(c, end = '')

# 任务3
phrase = "A bird in hand..."
for c in phrase:
    char = ''
    if c == 'A' or c == 'a':
        char += "X"
    else:
        char += c
    print(char, end = '')


# 8.70 更复杂的for循环
# 任务1
choices = ['披萨', '派', '沙拉', '薯条']
print('菜单：')
for index, item in enumerate(choices):
    print(index, item)

# 任务2
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
    if a > b:
        print(a)
    else:
        print(b)

# 任务3
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
list_c = [1, 5, 20, 6]
for a, b, c in zip(list_a, list_b, list_c):
    if a < b and b < c:
        print(a)
    elif b < a and b < c:
        print(b)
    else:
        print(c) 