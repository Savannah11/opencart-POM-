# utilities/config_reader.py
#读取配置文件数据
import json
import os
import yaml
from typing import Dict,Any

class ConfigReader:
    """多格式配置文件读取工具"""
    #静态方法不需要实例化可以直接调用，实例化后也能调用，可以理解成函数。括号后面不需要self参数
    @staticmethod
    def _read_yaml(file_path: str) -> Dict:
        import yaml
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)

    @staticmethod
    def _read_ini(file_path: str) -> Dict:
        from configparser import ConfigParser
        config = ConfigParser()
        config.read(file_path)
        return {section: dict(config.items(section)) for section in config.sections()}

    @staticmethod
    def _read_json(file_path:str) -> Dict:
        #json.load()是用来读取文件的，即，将文件打开然后就可以直接读取
        with open(file_path,'r',encoding='utf-8') as f:
            return json.load(f)
        #json.loads()是用来读取字符串的，即，可以把文件打开，用readline()读取一行，然后json.loads()一行

    @staticmethod
    def _read_yaml(file_path: str) -> Dict:
        import yaml
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)

    @staticmethod
    def _read_ini(file_path: str) -> Dict:
        from configparser import ConfigParser
        config = ConfigParser()
        config.read(file_path)
        return {section: dict(config.items(section)) for section in config.sections()}

# if __name__ == "__main__":
#     print(os.getcwd())
#     config = ConfigReader._read_json("../config/config.json")
#     print(config)
#     print(config["base_url"])