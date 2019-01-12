import os

base = {
    'servers':[
              {'index':0,
               'name': '12km_cluster_redis', 
              'host': os.environ.get('REDIS_HOST', '127.0.0.1'),
              'port': os.environ.get('REDIS_PORT', 6379),
              'databases':16
              },
          ],
    'seperator' : ':',
    'maxkeylen' : 100
}
media_prefix = "pyred_media"

host = '0.0.0.0'
port = 8085
debug = True

scan_batch = 10000
show_key_self_count = False

lang = 'zh_CN'

admin_user = os.environ.get('ADMIN_USER', 'admin')
admin_pwd = os.environ.get('ADMIN_PWD', 'admin')