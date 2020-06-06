from project import db


class Devices(db.Model):
    __tablename__ = 'devices'
    device_id = db.Column(db.Integer(), primary_key=True)
    unique_id = db.Column(db.String(100), unique=True)

    def __init__(self, unique_id):
        self.unique_id = unique_id

    def __repr__(self):
        return '<Device %r>' % self.unique_id
