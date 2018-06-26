import os

class Configuration(object):
    DEBUG = True
    PORT = int(os.getenv('PORT','22222'))
    HOST = '140.86.15.104'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://' \
            + os.getenv('MYSQLCS_USER_NAME','Captain') + ':' \
            + os.getenv('MYSQLCS_USER_PASSWORD','welcome1') + '@' \
            + os.getenv('MYSQLCS_CONNECT_STRING', \
            '140.86.15.104/deathstar')
