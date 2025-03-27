#实现数据、参数、方法、函数的共享
#专门存放fixture的文件
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from utilities.config_reader import ConfigReader
import logging
@pytest.fixture(scope='session',autouse=True)
def logging_config():
    #这个格式将会在日志记录中包含时间、模块名称、日志级别和日志信息。
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        # filename = 'test_log.log',  # 指定日志文件名称
        # filemode = 'w'  # 将日志写入文件（'w' 表示覆盖写入，'a' 表示追加写入）
        handlers=[
            logging.FileHandler('logs/test.log', mode='w',encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

    #******************************
    logging.getLogger().setLevel(logging.INFO) # 确保根日志记录器的级别设置正确
    logging.info('配置日志成功')

#作用域session  在整个测试会话期间，fixture 只会被创建一次。生命周期长，所有测试用例共享同一个 fixture 实例。
#适用于多个测试用例之间共享资源或状态
@pytest.fixture(scope='session',autouse=False)
def get_config():
    config = ConfigReader._read_json('config/config.json')
    return config

@pytest.fixture(scope='function',autouse=True)
def driver(get_config,request):
    print('执行用例前执行')
    # 参数request是pytest提供的一个内置fixture，用于获取测试用例的信息。
    # 手动处理 Unicode 转换  解决打印日志不显示中文问题
    test_name = request.node.name.encode('utf-8').decode('unicode_escape')
    logging.info(f"开始测试: {test_name}")
    driver = browser(get_config)
    yield driver
    logging.info(f"结束测试: {test_name}")
    print('执行用例后执行')
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# 钩子函数：pytest_runtest_makereport捕获测试结果并保存到item属性中，以便后续访问。
def pytest_runtest_makereport(item,call):
    # 获取测试结果并保存到item中
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
    return report
@pytest.fixture(autouse=True)
def screenshot_on_failure(request):
    yield
    # 在测试结束后检查是否失败
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        # 获取driver实例
        driver = request.getfixturevalue('driver')
        # 截图并附加到Allure报告
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name='failure_screenshot',
            attachment_type=allure.attachment_type.PNG
        )



def browser(config):
    q1 = Options()
    #保持浏览器打开状态
    q1.add_experimental_option(name='detach',value=True)
    #浏览器兼容性
    q1.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=Service(config["web_driver"]),options=q1)
    logging.info(f"进入页面 {config['base_url']}")
    driver.get(config["base_url"])
    #设置隐式等待时间 等待一定时间找不到元素则报错 （防止网络不佳而直接操作元素等情况）
    driver.implicitly_wait(config["implicitly_wait"])
    return driver