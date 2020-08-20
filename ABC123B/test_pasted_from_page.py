#
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#  
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        print(out)
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """29
20
7
35
120"""
        output = """215"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """101
86
119
108
57"""
        output = """481"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123
123
123
123
123"""
        output = """643"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
