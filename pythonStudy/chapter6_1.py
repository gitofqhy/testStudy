# 6.20练习：算分数
lilei = {"name": "Lilei", "homework": [], "quizzes": [], "tests": []}
hanmeimei = {"name": "Hanmeimei", "homework": [], "quizzes": [], "tests": []}
jim = {"name": "Jim", "homework": [], "quizzes": [], "tests": []}

lilei["homework"] = [90, 97, 75, 92]
lilei["quizzes"] = [88, 40, 94]
lilei["tests"] = [75, 90]

hanmeimei["homework"] = [100, 92, 98, 100]
hanmeimei["quizzes"] = [82, 83, 91]
hanmeimei["tests"] = [89, 97]

jim["homework"] = [0, 87, 75, 22]
jim["quizzes"] = [0, 75, 78]
jim["tests"] = [100, 100]

students = [lilei, hanmeimei, jim]
for student in students:
    print(student["name"], student["homework"], student["quizzes"], student["tests"])


def average(numbers):
    """
    求列表中数据的平均值
    :param numbers: 列表
    :return: 返回列表的平均值
    """
    total = sum(numbers)  # 求和
    return total / len(numbers)  # len统计列表中元素的个数


def get_average(student):
    """
    按权值计算学生最终的分数
    :param student: 学生分数信息字典
    :return: 返回学生最终的分数
    """
    homework = average(student["homework"])  # 计算平均分
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    homework *= 0.1  # 权重
    quizzes *= 0.3
    tests *= 0.5
    return homework + quizzes + tests


def get_letter_grade(score):
    """
    按照分数划分等级
    :param score: 分数
    :return: 分数对应的等级
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def get_class_average(class_list):
    """
    计算班级平均分
    :param class_list: 学生成绩字典
    :return: 返回班级学生平均分
    """
    results = []
    for student in class_list:
        results.append(get_average(student))
    return round(average(results), 2)


print("班级平均分：{}".format(get_class_average(students)))

for student in students:
    print("{}的平均分：{} ,平均等级：{}".format(student["name"], get_average(student), get_letter_grade(get_average(student))))

