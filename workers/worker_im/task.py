from __future__ import print_function
from __future__ import print_function
from __future__ import absolute_import

import json
import sys
from app import app
import time

sys.path.append("..")

from chromeos_builder.build_images.build_image_arm import build_image

JSONFilePath = '/home/jiahao/workspace/celery_cros_test/config.json'

# def readParams(path):
#     with open(path) as fin:
#         data = fin.read()
#     return json.loads(data)
#
# def writeParams(path, params):
#     with open(path, 'w') as fout:
#         data = json.dumps(params, sort_keys=True,
#                           indent=4)
#         fout.write(data)
#         print("wrote")
#         print(data)
#
# initial_parameter = readParams(JSONFilePath)

# @app.task
# def build_pac(ver, xml_no, board):
#     bi = build_image(ver, xml_no, board)
#     info = {
#         "ver":ver,
#         "xml_no":xml_no,
#         "board":board
#     }
#     bi.build_1()
#     # bi.build_2()
#     return json.dumps({'status':'success', 'info':info})

@app.task
def build_im(ver, xml_no, board):
    bi = build_image(ver, xml_no, board)
    info = {
        "ver":ver,
        "xml_no":xml_no,
        "board":board
    }
    # bi.build_1()
    bi.build_2()
    return json.dumps({'status':'success', 'info':info})
