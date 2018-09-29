# 6.10练习：水果店
# 计算客户购买水果时需要支付的金额
prices = {
    # 水果的价格
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    # 水果的库存
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
def list_fruit(prices, stock):
    """
    打印水果的名称、售价、库存
    :param prices: 水果的价格
    :param stock: 水果的库存
    :return:
    """
    for name in prices:
        print(name)
        print("售价 {}".format(prices[name]))
        print("现有数量 {}".format(stock[name]))

list_fruit(prices, stock)

def total_money(price, stock):
    """
    计算如果卖完总的水果能得到多少钱
    :param prince:
    :param stock:
    :return:
    """
    total_cost = 0
    for key in price:
        total_cost += price[key] * stock[key]
    return total_cost


print("总金额： {}".format(total_money(prices, stock)))


food = {  # 购买的水果及数量
    "banana": 8,
    "orange": 2,
    "apple": 3
}


def compute_bill(food, prices, stock):
    """
    购买列表中的水果需要支付的总价
    :param food: 购买列表
    :param prices: 水果价格
    :param stock: 水果库存
    :return: 购买列表中的水果需要支付的总价
    """
    total_cost = 0
    for key in food:
        if stock[key] > 0:
            if food[key] <= stock[key]:
                total_cost += prices[key] * food[key]
                stock[key] -= food[key]
            else:
                total_cost += prices[key] * stock[key]
                stock[key] = 0
    return total_cost


print("购买列表中的水果需要支付的总价：{}元".format(compute_bill(food, prices, stock)))

