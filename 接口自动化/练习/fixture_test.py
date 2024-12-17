#coding:utf-8
import pytest


class Test_1:

    def test_1(self):
        print("用例1-1")

    def test_2(self):
        print("用例1-2")

    def test_3(self):
        print("用例1-3")

class Test_2:

    def test_2_1(self):
        print("用例2-1")

    @pytest.mark.usefixtures("t2")
    def test_2_2(self):
        print("用例2-2")

    def test_2_3(self):
        print("用例2-3")

if __name__ == '__main__':
    pytest.main(['-vs'])