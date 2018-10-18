# 11.20 定义一个类
class Animal(object):
    is_alive = True  # 类变量
    health = "good"
    def __init__(self, name, age, is_hungry):
        self.name = name   # 实例变量
        self.age = age
        self.is_hungry = is_hungry

    def description(self):
        print(self.name)
        print(self.age)

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, False)
print(zebra.name, zebra.age, zebra.is_hungry)
print(giraffe.name, giraffe.age, giraffe.is_hungry)
print(panda.name, panda.age, panda.is_hungry)

print(Animal.is_alive)  # 类变量
print(zebra.is_alive)
print(giraffe.is_alive)
print(panda.is_alive)

# 当修改其中一个 对象名.类变量名时，
# 不会影响其他对象里的这个变量值
zebra.is_alive = False
print(Animal.is_alive)  # 类变量
print(zebra.is_alive)
print(giraffe.is_alive)
print(panda.is_alive)


# 而一旦修改 类名.类变量名的值
# 则所有对象的这个变量的值都被改变了
Animal.is_alive = False
print(Animal.is_alive)  # 类变量
print(zebra.is_alive)
print(giraffe.is_alive)
print(panda.is_alive)


# 11.40 类的方法
hippo = Animal("ab", 1, True)
hippo.description()
sloth = Animal("a", 2, True)
ocelot = Animal("b", 3, False)
print(hippo.health)
print(sloth.health)
print(ocelot.health)


class ShoppingCart(object):
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.item_in_cart = {}

# 向购物车里添加商品
    def add_item(self, product, price):
        if not product in self.item_in_cart:
            self.item_in_cart[product] = price
            print("{}加入了购物车.".format(product))
        else:
            print("{}本来就在购物车里".format(product))

# 从购物车里移出商品
    def remove_item(self, product):
        if product in self.item_in_cart:
            del self.item_in_cart[product]
            print("{}被移出了购物车".format(product))
        else:
            print("{}不在购物车里".format(product))


my_cart = ShoppingCart("Alice")
my_cart.add_item("大白菜", 4)
my_cart.add_item("柚子", 4)
my_cart.add_item("柚子", 4)
my_cart.remove_item("苹果")
my_cart.remove_item("大白菜")


# 11.50 类的继承
'''
class Shape(object):
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
'''


class Employee(object):
    def __init__(self, employee_name, hours):
        self.employee_name = employee_name
        self.hours = hours

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):   # 方法重写
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):   # 方法重写后访问父类方法
        self.hours = hours
        return super(PartTimeEmployee, self).calculate_wage(hours)


jim = Employee("Jim", 8)
bob = PartTimeEmployee("Bob", 4)
print(jim.calculate_wage(2))
print(bob.calculate_wage(2))
print(bob.full_time_wage(10))


# 11.60类的复习
class Triangle(object):
    number_of_sides = 3

    def __init__(self, angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False


class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle


my_triangle = Triangle(90, 30, 60)
equilateral_side_triangle = Equilateral()

print(my_triangle.number_of_sides)
print(my_triangle.check_angles())
print(equilateral_side_triangle.check_angles())
