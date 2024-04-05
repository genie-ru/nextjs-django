from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Mysqlの為の設定
        'NAME': 'app',                        # DB名
        'USER': 'root',                       # ユーザー名
        'PASSWORD': 'password',               # パスワード
        'HOST': 'host.docker.internal',       # コンテナからホストを参照し、backendコンテナからホストの53306ポートのMySQLに接続
        'PORT': '53306',                      # ポート番号
        'ATOMIC_REQUESTS': True               # トランザクションを自動でコミット
    }
}