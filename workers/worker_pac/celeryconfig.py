# celeryconfig.py
# coding=utf-8
from kombu import Queue,Exchange
# Broker 设置 RabbitMQ
BROKER_URL = 'redis://localhost'
CELERY_RESULT_BACKEND = 'redis://localhost/0'
CELERYD_PREFETCH_MULTIPLIER=2

# Tasks 位于 worker.py 中
# CELERY_IMPORTS = ('worker', )

# 默认为1次/秒的任务
# CELERY_ANNOTATIONS = {'worker.divide': {'rate_limit': '1/s'}}

# CELERY_ROUTES = {'worker.divide': {'queue': 'divide'},
#                  'worker.error_handler': {'queue': 'error'}}

# 默认所有格式为 json
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json', 'msgpack']
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYD_MAX_TASKS_PER_CHILD=1
worker_max_tasks_per_child=1

CELERY_QUEUES =  (
  Queue('buildPac',Exchange='agent',routing_key='buildPac'),
  Queue('buildIm',Exchange='agent',routing_key='buildIm'),
)