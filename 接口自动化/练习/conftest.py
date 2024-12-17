#coding:utf-8
import pytest

@pytest.fixture(scope="session",autouse=True)
def test_p():
    print("开始前")
    yield
    print("结束后")


@pytest.fixture()
def t2():
    print("不需要参数")
    T = 2
    Y = 3
    return T,Y