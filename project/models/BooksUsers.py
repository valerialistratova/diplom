from project import db


class BooksUsers(db.Model):
    __tablename__ = 'books_users'
    id = db.Column(db.Integer(), primary_key=True)
    bookmarked_id = db.Column(db.Integer())
    user_id = db.Column(db.Integer())

    def __init__(self, bookmarked_id, user_id):
        self.bookmarked_id = bookmarked_id
        self.user_id = user_id

    def __repr__(self):
        return '<User Id %r>' % self.user_id