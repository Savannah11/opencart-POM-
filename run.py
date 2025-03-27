#执行入口
import os
import pytest
import time

if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system('allure generate ./temps -o ./reports --clean')