#
from collections import deque
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#  
import sys
from io import StringIO
import unittest
import collections
import numpy as np

que = collections.deque([range(100)])
deque
array = np.array([range(1, 4)])

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """4 12 20"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14 14 14"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """454 414 444"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
