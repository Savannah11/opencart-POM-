import allure
import logging
import pytest
from poms.searchPage import SearchPage
#业务逻辑
#不需要导入confest，pytest会自动识别该文件
@pytest.mark.parametrize(
    'search_content',
    ['春季上新'])
@allure.epic('项目名称：opencart测试')
class TestSearch:

#     def test_search(self,driver,get_config,logging_config,search_content,request):
#         # logging.info(f"debug: {request.node.name}")
#         # search_content = '春季上新'
#         allure.dynamic.feature('模块名称:商品管理')
#         allure.dynamic.story('页面名称：商城首页')
#         allure.dynamic.title('用例名称：商品查询')
#         driver = driver
#         search_page = SearchPage(driver,get_config)
#         logging.info(f"搜索：'{search_content}'")
#         search_page.search(self.search_xpath,self.search_btn_xpath,search_content)

    def test_search_fail(self,driver,get_config,logging_config,search_content,request):
        search_page = SearchPage(driver, get_config)
        # search_content = '春季上新'
        logging.info(f"搜索：'{search_content}'")
        search_page.search(search_content)
        assert False