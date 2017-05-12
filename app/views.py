from app import app
from flask import render_template,request, jsonify
from app.models import Task
from datetime import datetime
from workers.worker_im.task import build_im
from workers.worker_pac.task import build_pac


list = {}

@app.route('/')
def index():
    return render_template("index.html")


# add delete update list

@app.route('/add', methods=['POST',])
def add():
    form = request.form
    version = form.get('version')
    board = form.get('board')
    id = build_pac.apply_async(args=['57', version, board],queue='buildPac',routing_key='buildPac')
    id = build_pac.apply_async(args=['57', version, board], queue='buildIm',routing_key='buildIm')
    task_id = "afagasgsgasfas"
    todo = Task(task_id=task_id, version=version, board=board, time=datetime.now())
    todo.save()
    print("sending task ver: %s board: %s" % (version, board))
    return jsonify(status="success")
#
#
# @app.route('/delete/<string:todo_id>')
# def delete(todo_id):
#     todo = Todo.objects.get_or_404(id=todo_id)
#     todo.delete()
#     return jsonify(status="success")
#
#
# @app.route('/update', methods=['POST',])
# def update():
#     form = request.form
#     todo_id = form.get('id')
#     status = form.get('status')
#     todo = Todo.objects.get_or_404(id=todo_id)
#     todo.status = status
#     todo.save()
#     return jsonify(status="success")
#
@app.route('/list')
def list():
    '''
        <th data-field="task_id">Task ID</th>
        <th data-field="version">Version</th>
        <th data-field="board">Board</th>
        <th data-field="status">Status</th>
        <th data-field="date">Date</th>
    :return: json
    '''
    tasks = Task.objects.order_by('-time')
    # res = [task.to_json() for task in tasks]
    for item in tasks:
        item['status'] = 'pending'
    res = [task.to_json() for task in tasks]
    return jsonify(res)
    # res = [
    #     {
    #         'task_id': 'afafasfasfa',
    #         'version': '57',
    #         'board': 'cyan',
    #         'status': 'success',
    #         'date': '12344556'
    #     },
    #     {
    #         'task_id': 'afafasfasfa',
    #         'version': '57',
    #         'board': 'cyan',
    #         'status': 'success',
    #         'date': '12344556'
    #     },
    #     {
    #         'task_id': 'afafasfasfa',
    #         'version': '57',
    #         'board': 'cyan',
    #         'status': 'success',
    #         'date': '12344556'
    #     },
    #     {
    #         'task_id': 'afafasfasfa',
    #         'version': '57',
    #         'board': 'cyan',
    #         'status': 'success',
    #         'date': '12344556'
    #     },
    #     {
    #         'task_id': 'afafasfasfa',
    #         'version': '57',
    #         'board': 'cyan',
    #         'status': 'success',
    #         'date': '12344556'
    #     },
    #     {
    #         'task_id': 'afafasfasfa',
    #         'version': '57',
    #         'board': 'cyan',
    #         'status': 'success',
    #         'date': '12344556'
    #     }
    # ]
    # # item = {
    # #     'task_id':'afafasfasfa',
    # #     'version':'57',
    # #     'board':'cyan',
    # #     'status':'success',
    # #     'date':'12344556'
    # # }
    # return jsonify(res)


