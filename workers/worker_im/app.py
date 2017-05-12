from __future__ import absolute_import

import json

from celery import Celery

JSONFilePath = '../config.json'

app = Celery('worker_im', include=['task'])
app.config_from_object('celeryconfig')




if __name__ == '__main__':
    # params = readParams(JSONFilePath)
    app.start()