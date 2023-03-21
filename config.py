DEBUG = True
JSON_AS_ASCII = False

#数据库配置
DB_URI = 'mysql://user:pass@localhost/dbname'


try:
    from local_config import *  # NOQA
except ImportError as e:
    print('Import from local_config failed, %s' % str(e))