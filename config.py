class config(object):
    JSON_TO_ASCII = False
    SECRET_KEY = 'secret2022'

    HOSTNAME = '47.112.216.3'
    PORT = '3306'
    DATABASE = 'ifhs_db'
    USERNAME = 'root'
    PASSWORD = 'mysql1010'
    DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = True
