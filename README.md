# 🚀 opencart自动化基础pom框架

基于selenium+pytest+allure的POM自动化框架，简单示例opencart购物车搜索功能测试。

## ✨ Key Features

*   **核心特性 1:** pom框架实现业务逻辑与页面元素的解耦，降低维护成本。封装页面元素定位及操作方法，增强代码复用性。形成基类-页面类-测试类的清晰三层架构。
*   **核心特性 2:** 利用allure自动生成测试报告，可视化测试结果，支持错误截图，更快捷定位问题。
*   **核心特性 3:** 显示等待控制元素符合特定条件后进行操作，减少无效等待时间。异常处理防止长时间等待、卡死。

### Prerequisites

*   Python 3.13,jdk21

### Installation
```bash
# 选择一种适合你项目的安装方式
 或者从源码安装
git clone git@github.com:Savannah11/opencart-POM-.git
cd /opencart-POM-
pip install -r requirements.txt
```
