"""
配置
"""


class BaseConfig():
    ES_HOST = '192.168.85.129'
    ES_PORT = 9200


class Development(BaseConfig):
    DEBUG = True


class TEST(BaseConfig):
    DEBUG = False


class Product(BaseConfig):
    DEBUG = False


setting = {
    'dev': Development,
    'test': TEST,
    'pro': Product
}

conf = setting['dev']()






