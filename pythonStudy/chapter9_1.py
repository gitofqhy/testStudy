from random import randint
# 附加题1  10 * 5的地图，5条船
# print([1, 2] == [1, 3])
board = []
print(["O"] * 5)
for i in range(10):
    board.append(['O'] * 5)
print(board)

def print_board(board_in):
    """
    绘制地图
    :param board_in:
    :return:
    """
    for row in board:
        print(' '.join(row))  # 列表元素拼接成字符串
print_board(board)
#print(len(board[0]))
def random_row(board_in):
    """
    行的随机数
    :param board_in:
    :return:
    """
    return randint(0, len(board_in) - 1)

def random_col(board_in):
    """
    列的随机数
    :param board_in:
    :return:
    """
    return randint(0, len(board_in[0])-1)

ship = []
for i in range(5):
    ship_row = random_row(board)
    ship_col = random_col(board)
    ship.append([ship_row, ship_col])
print(ship)

def test_ship(ship, guess_row, guess_col):
    """
    判断所猜的坐标是否船的坐标
    :param ship: 5艘船的位置
    :param guess_row: 猜测的行
    :param guess_col: 猜测的列
    :return:
    """
    count = 0
    for i in ship:
        if i == [guess_row, guess_col]:
            return True
        else:
            count += 1
    if count == 5:
        return False

for turn in range(10):
    print("Turn", turn + 1)
    guess_row = int(input("猜一下船在第几行：")) - 1
    guess_col = int(input("猜一下船在第几列：")) - 1

    if test_ship(ship, guess_row, guess_col):
        print("恭喜，你击落了我的战船！")
        break
    elif guess_row not in range(10) or guess_col not in range(5):
        print("输入的行列超出了地图范围了。")
    elif board[guess_row][guess_col] == "X":
        print("这个位置已经猜过了。")
    else:
        print("你没有击中我的战船！")
        board[guess_row][guess_col] = "X"
        print_board(board)
    if turn == 9:
        print("Game Over")
