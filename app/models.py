from app import db
import datetime


class Task(db.Document):
    task_id_pac = db.StringField(required=True)
    task_id_im = db.StringField(required=True)
    version = db.StringField(required=True, max_length=20)
    board = db.StringField(required=True)
    time = db.DateTimeField(default = datetime.datetime.now())
    status = db.StringField(required=True)

    def to_json(self):
        return {
            'id': str(self.id),
            'task_id_im' : str(self.task_id_im),
            'task_id_pac': str(self.task_id_pac),
            'version': self.version,
            'board': self.board,
            'time': self.time,
            'status': self.status
        }


