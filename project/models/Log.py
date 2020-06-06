from project import db


class Log(db.Model):
    __tablename__ = 'log'
    log_id = db.Column(db.Integer(), primary_key=True)
    device_id = db.Column(db.Integer(), unique=False)
    book_id = db.Column(db.Integer(), unique=False)
    datetime = db.Column(db.DateTime())
    progress = db.Column(db.Float())

    def __init__(self, device_id, book_id, datetime, progress):
        self.device_id = device_id
        self.book_id = book_id
        self.datetime = datetime
        self.progress = progress

    def __repr__(self):
        return '<User %r>' % self.datetime