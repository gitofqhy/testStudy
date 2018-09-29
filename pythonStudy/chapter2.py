# 转义字符
print('There\'s a sanke in my boot!')
print("There's a snake in my boot!")

# 字符串索引
fifth_letter = "MONTY"[-1]
print(fifth_letter)

# 字符串方法
game = "I like Wangzhe!"
print(game)
print(len(game))  # 计算字符串长度
print(game.lower())  # 转换成小写
print(game.upper())  # 转换成大写
pi = 3.14
print(str(pi))  # 转换成字符串

# 字符串拼接
print("Good" + "good" + "study!")  # python2、python3通用
print("{} {} {}!".format("Good", "good", "study"))  # python3推荐写法
print("{2} {1} {0}!".format("Good", "good", "study"))  # 加上数字表示用第几个字符串来替换这个占位符
print("煎饼" + "果子")
print("{}{}".format("煎饼", "果子"))
print("我每顿吃" + str(2) + "个包子")
print("{}{}{}".format("我每顿吃", 2, "个包子"))  # format方法可自动把数字转换成字符串
print("{}{:.3f}{}".format("我每顿吃", 2.56387, "个包子"))  # 保留3位小数
'''
name = input("你叫什么名字？")
quest = input("你多高？")
color = input("你喜欢吃什么？")
print("你叫{}，身高{},喜欢吃{}.".format(name, quest, color))
'''

# 复习
my_word = "huaying"
print(my_word)
print(my_word.upper())
print(my_word.capitalize())  # 把字符串的第一个字符转换成大写
print(my_word.count("h"))
print(my_word.find("i"))
print(my_word.index('h'))
'''
string.find(str, beg=0, end=len(string))
#检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定 范围内，如果是返回开始的索引值，否则 返回-1
string.index(str, beg=0, end=len(string))
#跟find()方法一样，只不过如果str不在 string中会报一个异常.

'''
print(my_word.join("***"))
'''
string.join(seq)
#Merges (concatenates)以 string 作为分隔 符，将 seq 中所有的元素(的字符串表示)合 并为一个新的字符串
'''
# 字符串内建函数：https://www.cnblogs.com/liuzhenhua0122/p/6690058.html
