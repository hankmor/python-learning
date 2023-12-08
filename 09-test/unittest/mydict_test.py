"""
单元测试
python 从语言层面支持单元测试，首先需要编写单元测试文件，然后发起单元测试可以通过 python -m unittest xxx.py 来执行，
也可以通过 unittest.main() 来执行
"""

import unittest
from mydict import MyDict


class MyDictTest(unittest.TestCase):
    """ MyDict 单元测试类，继承自 unittest.TestCase """

    def setUp(self):
        """ 每一个单元测试方法开始前执行 """
        print("setUp")

    def tearDown(self):
        """ 每一个单元测试方法结束后执行 """
        print("tearDown")

    def test_init(self):
        """ 测试创建 """
        d = MyDict(a=1, b="str")
        # 使用 unittest 包的 assertXxx 方法做断言
        self.assertEqual(d["a"], 1)
        self.assertEqual(d.a, 1)
        self.assertTrue(d.a == d["a"])

    def test_attr(self):
        """ 属性读写测试 """
        d = MyDict()
        # MyDict 支持赋值
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
        self.assertEqual(d.key, 'value')

    def test_key_error(self):
        """ 测试读取不存在的 key 时是否正确抛出异常 """
        d = MyDict()
        # 如果通过 dict 方式读取不存在的 key 则会抛出 KeyError，而会被 with 语句捕获
        with self.assertRaises(KeyError):
            v = d["notExists"]

    def test_attr_error(self):
        """ 测试按照属性读取不存在的 key 时是否能够正确抛出异常 """
        d = MyDict()
        # 如果通过属性方式读取不存在的 key 则会抛出 AttributeError，而会被 with 语句捕获
        with self.assertRaises(AttributeError):
            v = d.notExists


# 还可以通过在 terminal 执行 python3 -m unittest mydict_test.py 启动测试
if __name__ == '__main__':
    """ 运行单元测试 """
    unittest.main()
