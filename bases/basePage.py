from selenium.webdriver.common.by import By
#
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from utilities.config_reader import ConfigReader

#封装selenium方法
class BasePage:
    def __init__(self,driver,config):
        self.driver = driver
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
   #定位单个元素
    def find_ele(self,xpath):
        try:
            self.driver.implicitly_wait(self.config["implicitly_wait"])
            return self.driver.find_element(By.XPATH,xpath)

        except Exception:
            print('元素定位失败',xpath)
            pic = self.config['screen_path']+'search_box.png'
            self.driver.save_screenshot(pic)
            self.logger.info(f"元素定位失败，截图已保存至 {self.config['screen_path']}")
    #定位多个元素，多个返回列表
    def find_eles(self,xpath):
        try:
            self.driver.implicitly_wait(10)
            return self.driver.find_element(By.XPATH,xpath)
        except Exception:
            print('元素定位失败',xpath)
            self.logger.info(f"Element not found: {xpath}")
