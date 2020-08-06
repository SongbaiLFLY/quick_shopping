"""
基础配置信息
通过 configs/__init__.py 将这个模块设置为默认的 config
"""
DEBUG = True
STAGE = 'develop'

# sanic server config
HOST = '0.0.0.0'
PORT = 8000
WORKERS = 1

# jwt secret
JWT_SECRET = 'J2dfYmXuPgtF-1KhMk01MpT3pneSAUutp5fNNT9vPrdyJN1TD9'
# 登陆 token 失效时间
JWT_SESSION_EXP = 2 * 24 * 60 * 60
# 验证码 token 过期时间
JWT_CODE_EXP = 3 * 60

# 验证码记录时间
CODE_RECORD_TTL = 3 * 60

# cassandra config
CASSANDRA_NODES = ['cassandra']
CASSANDRA_REPLICATION_FACTOR = 1

CASSANDRA_KEYSPACE = 'quick_shopping_sanic'

# rabbitmq
RABBITMQ_HOSTNAME = 'rabbitmq'
RABBITMQ_PORT = 5672
RABBITMQ_EXCHANGE = 'quick_shopping'
RABBITMQ_QUEUE = 'quick_shopping'
RABBITMQ_ROUTING_KEY = 'quick_shopping'

# role
ROLE_USER = 'USER'
ROLE_DEVELOPER = 'DEVELOPER'
ROLE_MANAGER = 'MANAGER'

# 有权限的身份
ROLES = [ROLE_USER, ROLE_DEVELOPER, ROLE_MANAGER]

# RPC hostname
CREATE_PROFILE_URL = 'http://quick_shopping:8000/v1/profile'

# email config
EMAIL_ADDRESS = ''
EMAIL_PASSWORD = ''
