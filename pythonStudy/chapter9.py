from random import randint
# 9.10战船1   5 * 5的地图
# print(["O"] * 5)
board = []
for i in range(0, 5):
    board.append(["O"] * 5)
# print(board)
def print_board(board_in):
    """
    绘制地图
    :param board_in:
    :return:
    """
    for row in board:
        print(' '.join(row))  # 列表元素拼接成字符串
print_board(board)

# 9.20战船2
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
    return randint(0, len(board_in)-1)

#print(random_row(board))
#print(random_col(board))

ship_row = random_row(board)
ship_col = random_col(board)
#print(ship_row + 1)
#print(ship_col + 1)
for turn in range(4):
    print("Turn", turn + 1)
    guess_row = int(input("猜一下船在第几行：")) - 1
    guess_col = int(input("猜一下船在第几列：")) - 1
    if guess_row == ship_row and guess_col == ship_col:
        print("恭喜，你击落了我的战船！")
        break
    elif board[guess_row][guess_row] == "X":
        print("这个位置已经猜过了。")
    else:
        if guess_row not in range(4) or guess_col not in range(4):
            print("输入的行列超出了地图范围了。")
        else:
            print("你没有击中我的战船！")
            board[guess_row][guess_row] = "X"
            print_board(board)
    if turn == 3:
        print("Game Over")


