# 12.10 写文件
my_list = [i ** 2 for i in range(1, 11)]
my_file = open("output.txt", "w")
for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()

# 读文件
my_file = open("output.txt", "r")
print(my_file.read())

my_file.close()

my_file = open("output.txt", "r")
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close()


write_file = open("output.txt", "w")
read_file = open("output.txt", "r")

write_file.write("没关闭会出问题")
write_file.close()
print(read_file.read())
read_file.close()

# 12.30用with读写文件
with open("test.txt", "w") as my_file:
    my_file.write("hello world")

f = open("test.txt")
# f.close()
if not f.closed:
    print(f.closed)
    f.close()
else:
    print(f.closed)
