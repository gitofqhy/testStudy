# 程序设计：Pig Latin翻译器
'''
    1.要求用户输入一个英文单词
    2.检查用户输入的值是否是一个英文单词
    3.把这个英文单词翻译成Pig Latin
    4.把翻译结果显示在屏幕上
'''
original = input("请输入一个英文单词：")
pyg = 'ay'
if len(original) > 0 and original.isalpha():
    #  print(original)  #验证长度和是否是纯字母
    word = original.lower()  # 把字符串转换成小写
    first = word[0]  # 取字符串的首字母
    new_word = word + first + pyg  # 拼接首字母和“ay”
    new_word = new_word[1:len(new_word)]  # 字符串切片，截取字符串第二个字符到最后的字母
    print(new_word)
else:
    print("输入的单词不合法")  