# 转换.py文件，即将目标文件转换成可单独执行的.py文件，命名为setup.py
from distutils.core import setup
import py2exe

setup(console=['test.py'])
