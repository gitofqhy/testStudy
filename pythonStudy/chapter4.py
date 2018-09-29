# 函数方法
def coupon(original_price):
    """
    每满80减20
    :param original_price: 原价
    :return: 折后价
    """
    new_price = original_price - int(original_price / 80) * 20
    print("选择满减优惠后的价格为：{}".format(new_price))
    return new_price


def dicount(original_price):
    """
    打85折
    :param original_price: 原价
    :return: 折后价
    """
    new_price = original_price * 0.85
    print("选择直接打折后的价格为：{}".format(new_price))
    return new_price


original_price = 315
price_that_use_coupon = coupon(original_price)
price_that_use_discount = dicount(original_price)


def cook():
    """
    输出"番茄加鸡蛋！"
    :return:
    """
    print("番茄加鸡蛋！")


cook()


def square(n):
    """
    计算一个数的平方
    :param n:
    :return: 这个数的平方值
    """
    squareed = round(n ** 2, 2)
    print("{}的平方是{}.".format(n, squareed))
    return squareed


my_number_square = square(10)
print(my_number_square)
square(13.52)
print(13.52 ** 2)

# 4.60 练习
def cube(n):
    """
    计算立方
    :param n:
    :return: 返回立方的值
    """
    return n ** 3
print(cube(2))

def test_three(n):
    """
    接收一个参数，如果输入的数字能被3整除，那么返回这个数的立方，否则返回False
    :param n:
    :return:
    """
    if n % 3 == 0:
        return cube(n)
    else:
        return False


print(test_three(3))


# 4.70模块的导入
import math  # 直接导库名
print(math.sqrt(25))

from math import sqrt  # 只import具体方法
print(sqrt(81))


# 更多的内建方法
def biggest_number(*args):
    """
    带*号的参数名表示传入值是一个元组，也就说这个方法可以接受任意数量的数字
    :param args:
    :return:
    """
    print(max(args))
    print(type(args))
    return max(args)


biggest_number(-10, -5, 5, 10, 20)


# 4.90练习
def shut_down(s):
    """

    :param s:
    :return: s = 'yes',返回“关闭执行中”；s = no,返回“已取消关闭操作”；其他，返回“对不起，无法执行”
    """
    if s == "yes":
        return "关闭执行中"
    elif s == "no":
        return "已取消关闭操作"
    else:
        return "对不起，无法执行"


print(shut_down("yes"))
print(shut_down("no"))
print(shut_down("y"))


from math import sqrt
print(sqrt(13689))

def distance_from_zero(num):
    """
    如果传入参数类型是int或float，返回传入参数的绝对值，否则返回“算不了”
    :param num:
    :return:
    """
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return "算不了"


print(distance_from_zero('11'))
print(distance_from_zero(-9))


# 4.100更多的练习
def hotel_cost(nights):
    """
    计算住宿费用，标准房488一晚
    :param nights: 住几晚
    :return: 返回所花的费用
    """
    return nights * 488

def train_cost(city):
    """
    计算高铁的费用
    :param city: 城市的名字
    :return: 返回到达输入的城市所需的费用
    """
    if city == "上海":
        return 92.5 * 2
    elif city == "南京":
        return 117.5 * 2
    elif city == "苏州":
        return 117.5 * 2
    elif city == "西安":
        return 653.5 * 2
    else:
        return "没有到达该城市的班次"


def rent_cat_cost(days):
    """
    计算租车费用
    :param days: 租车的天数
    :return: 返回租车的费用
    """
    if days > 7:
        return days * 78 - 67
    elif days > 3:
        return days * 78 - 20
    else:
        return days * 78


def trip_cost(city, days, spending_money):
    """
    计算旅行总花费
    :param city: 城市
    :param days: 旅行的天数
    :return: 返回旅行的总花费
    """
    return hotel_cost(days - 1) + train_cost(city) + rent_cat_cost(days) + spending_money


print("西安五日游总费用：{}".format(trip_cost("西安", 5, 3000)))
print("上海两日游总费用：{}".format(trip_cost("上海", 2, 4000)))




