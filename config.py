DEBUG = True
JSON_AS_ASCII = False

#数据库配置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'travel'
USERNAME = 'root'
PASSWORD = 'Monster5.'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

