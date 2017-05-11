from app import app
from flask import render_template,request, jsonify
# from app.models import Todo
from datetime import datetime


@app.route('/')
def index():
    return render_template("index.html")


# add delete update list

# @app.route('/add', methods=['POST',])
# def add():
#     form = request.form
#     content = form.get('content')
#     todo = Todo(content=content,time=datetime.now())
#     todo.save()
#     return jsonify(status="success")
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
    res = [
        {
            'task_id': 'afafasfasfa',
            'version': '57',
            'board': 'cyan',
            'status': 'success',
            'date': '12344556'
        },
        {
            'task_id': 'afafasfasfa',
            'version': '57',
            'board': 'cyan',
            'status': 'success',
            'date': '12344556'
        },
        {
            'task_id': 'afafasfasfa',
            'version': '57',
            'board': 'cyan',
            'status': 'success',
            'date': '12344556'
        },
        {
            'task_id': 'afafasfasfa',
            'version': '57',
            'board': 'cyan',
            'status': 'success',
            'date': '12344556'
        },
        {
            'task_id': 'afafasfasfa',
            'version': '57',
            'board': 'cyan',
            'status': 'success',
            'date': '12344556'
        },
        {
            'task_id': 'afafasfasfa',
            'version': '57',
            'board': 'cyan',
            'status': 'success',
            'date': '12344556'
        }
    ]
    # item = {
    #     'task_id':'afafasfasfa',
    #     'version':'57',
    #     'board':'cyan',
    #     'status':'success',
    #     'date':'12344556'
    # }
    return jsonify(res)


