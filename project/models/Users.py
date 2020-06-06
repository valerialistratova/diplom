from project import db


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer(), primary_key=True)
    device_id = db.Column(db.Integer(), unique=False)
    name = db.Column(db.String(200))
    photo = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(32))

    def __init__(self, device_id, name, photo, password):
        self.device_id = device_id
        self.name = name
        self.photo = photo
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name

