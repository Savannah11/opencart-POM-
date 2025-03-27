# import logging
#页面基本操作
import allure
from bases.basePage import BasePage
class SearchPage(BasePage):
    # 统一元素管理：将元素定位器集中定义在页面类顶部
    search_xpath = "//input[@type='text' and @class='form-control' and @placeholder='搜索']"
    search_btn_xpath = "//button[contains(@class,'btn btn-primary')]"
    @allure.step("搜索框输入‘{search_content}',并搜索")
    def search(self,search_content):
        search_box = self.find_ele(self.search_xpath)
        search_box.send_keys(search_content)
        self.logger.info(f"在元素'{self.search_btn_xpath}' 输入'{search_content}'")
        search_btn = self.find_ele(self.search_btn_xpath)
        search_btn.click()

    def take_screenshot(self)->bytes:
        return self.driver.get_screenshot_as_png()
