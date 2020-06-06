from project import db


class Books(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(500), unique=True)
    length = db.Column(db.Integer())
    photo = db.Column(db.String(100))
    isbn = db.Column(db.String(50))

    def __init__(self, title, length):
        self.title = title
        self.length = length

    def __repr__(self):
        return '<Book %r>' % self.title