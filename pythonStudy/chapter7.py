# 7.10 复习列表
# 任务1
n = [1, 3, 5]
print(n[1])  # 打印列表n的第二个元素

# 任务2
n[1] *= 5  # 把列表的第二个元素的值乘以5
print(n)

# 任务3
n.append(4)  # 在列表末尾插入一个元素4
print(n)

# 任务4
# 删除列表的方法
# del n[0]  # 删除列表的第一个元素
# n.pop(0)
n.remove(1)
print(n)


# 7.20复习方法
# 任务1
number = 5
def my_function(x):
    return x * 3
print(my_function(number))

# 任务2
m = 5
n = 13
def add_function(m, n):
    return m + n
print(add_function(m, n))

# 任务3
n = "Hello"
def string_function(s):
    return s + "word"
print(string_function(n))

# 任务4
def list_function(x):
    return x
n = [3, 5, 7]
print(list_function(n))

# 7.30列表加方法的练习1
# 任务1
def list_function(x):
    return x[1]
n = [3, 5, 7]
print(list_function(n))

# 任务2
def list_function(x):
    x[1] += 3
    return x
n = [3, 5, 7]
print(list_function(n))

# 任务3
n = [3, 5, 7]
def list_extender(lst):
    lst.append(9)
    return lst
print(list_extender(n))

# 任务4
n = [3, 5, 7]
def print_list(x):
    for i in x:
        print(i)
print_list(n)

# 任务5
n = [3, 5, 7]
def double_list(x):
    for i in range(0, len(x)):
        x[i] *= 2
    return x
print(double_list(n))


# 7.40列表加方法的练习2
# 任务1
def my_function1(x):
    for i in range(0, len(x)):
        x[i] = x[i]
    return x
print(my_function1([0, 1 , 2]))


# 任务2
def total(numbers):
    result = 0
    for number in numbers:
        result += number
    return result
n = [3, 5, 7]
print(total(n))

# 任务3
def join_strings(words):
    result = ""
    for word in words:
        result += word
    return result
n = ["Michael", "Lieberman"]
print(join_strings(n))

# 7.50列表加方法的练习3
# 任务1
def join_list(x, y):
    return x + y
m = [1, 2, 3]
n = [4, 5, 6]
print(join_list(m, n))

# 任务2
def flatten(lists):
    results = []
    for numbers in lists:
        for number in numbers:
            results.append(number)
    return results
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
print(flatten(n))
