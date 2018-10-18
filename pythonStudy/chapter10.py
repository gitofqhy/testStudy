# 10.10 操作符 in
my_dict = {1: 'a', 2: 'b', 3: 'c'}
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
for key in my_dict:
    print(key, my_dict[key])

# 10.20 构建列表
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)
cubes_by_four = [x ** 3 for x in range(1, 11) if x**3 % 4 == 0]
print(cubes_by_four)

# 10.30 带步长的切片
list_a = [i ** 2 for i in range(1, 11)]
print(list_a)
print(list_a[2: 9: 2])
print(list_a[2: 9: 4])

my_list = range(1, 11)
for i in my_list[0: 11: 2]:
    print(i)

letters = ['A', 'B', 'C', 'D', 'E']
print(letters[::-1])

for i in my_list[10:: -1]:
    print(i)

to_one_hundred = range(101)
for i in to_one_hundred[::-10]:
    print(i)

to_21 = [x for x in range(1, 22)]
odds = to_21[::2]
middle_third = to_21[int(len(to_21)/3): int(len(to_21)/3)*2]
print(to_21)
print(odds)
print(middle_third)

# 10.40匿名函数
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(list(filter(lambda s: s == "Python", languages)))

squares = [x**2 for x in range(1, 11)]
print(squares)
print(list(filter(lambda n: n >= 30 and n <= 70, squares)))
