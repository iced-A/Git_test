#coding:utf-8
import pytest,os,time
from common import yaml_util

#定义一个pytest的hook函数pytest_sessionfinish,在整个测试会话结束时调用,用于执行Allure生成报告命令
def pytest_sessionfinish(session,exitstatus):
    os.system("allure generate ./temp -o ./report --clean")


@pytest.fixture(scope="session",autouse=True)
def test_p():
    print("开始前初始话对应yaml文件数据")
    # yaml_util.YamlUtil().claer_extract_yaml(yaml_file)
    yield
    print("结束后")

@pytest.fixture()
def t2():
    print("不需要参数")
    T = 2
    Y = 3
    return T,Y


