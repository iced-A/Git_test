#coding:utf-8
import pytest
from common import yaml_util

@pytest.fixture(scope="session",autouse=True)
def test_p():
    print("开始前初始话对应yaml文件数据")
    yaml_util.YamlUtil().claer_extract_yaml()
    yield
    print("结束后")


@pytest.fixture()
def t2():
    print("不需要参数")
    T = 2
    Y = 3
    return T,Y


