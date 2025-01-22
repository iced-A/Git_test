#coding:utf-8
import pytest

class Test_Y:
    @pytest.mark.parametrize("t1",['1','2','3'])
    def test_1(self,t1):
        print(t1)

    @pytest.mark.parametrize("t2", [["小红",'11'],["小明",'12'],["小白",'13']])
    def test_2(self, t2):
        print(t2)

    @pytest.mark.parametrize("name,age", [["小红",'11'],["小明",'12'],["小白",'13']])
    def test_3(self,name,age):
        print(name,age)

if __name__ == '__main__':
    pytest.main(["-vs"])