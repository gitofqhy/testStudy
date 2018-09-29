# 5.10列表
breakfast = ["鸡蛋", "香蕉", "大饼", "煎饺"]
numbers = [5, 6, 7, 8]
print(numbers[1] + numbers[3])
print(breakfast)
breakfast[2] = "吐司"
print(breakfast)
breakfast[1] = "柚子"
print(breakfast)


# 追加元素
suitcase = []
suitcase.append("眼镜")
suitcase.append("钱包")
suitcase.append("雨伞")
suitcase.append("纸巾")
suitcase.append("唇膏")
list_length = len(suitcase)

print("手提箱里有{}件东西".format(list_length))
print(suitcase)


# 列表切片和字符切片
# 列表名[起始下标_含:结束下标_不含]
suitcase = ["眼镜", "帽子", "护照", "笔记本电脑", "外套", "鞋子"]
first = suitcase[0: 2]  # 取第一第二个元素
print(first)

middle = suitcase[2: 4]  # 取第三第四个元素
print(middle)

last = suitcase[4: 6]  # 取第五第六个元素
print(last)

first_half = suitcase[:3]  # 前半
print(first_half)

second_half = suitcase[3:]  # 后半
print(second_half)

# 反向切片
letters = "abcde"
slice = letters[:-3]
print(slice)
slice = letters[-3:]
print(slice)


# 5.40插入元素
animals = ["猫", "狗", "兔"]
print(animals.index('狗'))
animals.insert(1, '鸟')
print(animals)
animals.insert(animals.index('狗'), "牛")
print(animals)


# 5.50遍历
my_list = [1, 9, 3, 8, 5, 7]
for number in my_list:
    print(number * 2)

# 5.60排序
start_list = [5, 3, 1, 2, 4]
square_list = []
for num in start_list:
    square_list.append(num ** 2)
square_list.sort()
print(square_list)


# 5.70字典
phone_numbers = {"小红": 13712345678, "小明": 13712345678, "韩梅梅": 13787654321}
print(phone_numbers["小红"])
print(phone_numbers["小明"])
print(phone_numbers["韩梅梅"])

test_list = {1: 'a', 1:'b'}    # key不可以重复，如果重复会有一个值取不到
print(test_list[1])

num_list = {}
num_list[0] = 'aa'   # 字典插入
num_list[2] = 'bb'
num_list[3] = 'cc'
print(len(num_list))  # 打印字典元素个数

menu = {}
menu["蟹粉小笼"] = 49.50
menu["炒时蔬"] = 8.00
menu["青椒肉丝"] = 15.00
print("菜单上共有{}道菜".format(len(menu)))
print(menu)
menu["蟹粉小笼"] = 39  # 修改元素内容
print(menu)


# 5.80删除元素
number_list = [7, 1, 6, 1, 2, 2, 3, 4, 5]
number_list.remove(1)  # 删除值为1的元素
print(number_list)
del number_list[-2]  # 删除倒数第二个元素
print(number_list)

# 5.90遍历字典
d = {"foo": "bar", "foo2": "bar2"}
for key in d:
    print(d[key])
for key, value in d.items():
    print(key, value)

webster = {
    "Aardvark": "A star of a popular children's cartoon show.",
    "Baa": "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A samll amount."
}
for key in webster:
    print(webster[key])


# 5.100练习
inventory = {
    '零钱': 500,
    '小口袋': ['小刀', '绳子', '手套'],
    '大口袋': ['帐篷', '水杯', '睡袋', '毛巾']
}
inventory['零食'] = ['苹果', '面包', '牛奶']
print(inventory)
inventory['大口袋'].sort()
print(inventory)
inventory['大口袋'].remove('毛巾')
print(inventory)
inventory['零钱'] += 50
print(inventory)


# 5.110更多的练习
names = ["Adam", "Alex", "Mariah", "Martine", "Columbus"]
for name in names:
    print(name)


import keyword
print(keyword.kwlist)

#assert 2 == 1, "2不等于1"
add = lambda x, y: x + y
print(add(1, 2))

newlist = filter(lambda x: x % 3 == 0, [9, 6, 3])
print(newlist)

a = [1, 3, 4, 7]
for key in a:
    if key % 2 == 0:
        print(key)  # 打印出能被2整除的元素
'''
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = 'FizzBuzz'
    elif number % 3 == 0:
        number = 'Fizz'
    elif number % 5 == 0:
        number = 'Buzz'
    print(number)
'''

def fizz_count(x):
    """
    统计fizz在x中出现的次数
    :param x:
    :return:
    """
    count = 0
    for n in x:
        if n == 'Fizz':
            count += 1
    return count

numbers_list = []
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = 'FizzBuzz'
    elif number % 3 == 0:
        number = 'Fizz'
    elif number % 5 == 0:
        number = 'Buzz'
    numbers_list.append(number)
    print(number)
print(numbers_list)
print(fizz_count(numbers_list))

# 遍历字符串
for letter in "testup测试进阶":
    print(letter)
print()
print()

word = "Programming is fun!"
for letter in word:
    if letter == 'i':
        print(letter)
