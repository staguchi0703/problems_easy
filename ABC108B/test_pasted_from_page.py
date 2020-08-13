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
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """0 0 0 1"""
        output = """-1 1 -1 0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3 6 6"""
        output = """3 10 -1 7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31 -41 -59 26"""
        output = """-126 -64 -36 -131"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
