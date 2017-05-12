from app import db
import datetime


class Task(db.Document):
    task_id = db.StringField(required=True)
    version = db.StringField(required=True, max_length=20)
    board = db.StringField(required=True)
    time = db.DateTimeField(default = datetime.datetime.now())
    status = db.StringField(required=True)

    def to_json(self):
        return {
            'task_id': str(self.task_id),
            'version': self.version,
            'board': self.board,
            'time': self.time,
            'status': self.status
        }


