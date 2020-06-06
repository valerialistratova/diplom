from project import db


class UsersBooksRatings(db.Model):
    __tablename__ = 'users_books_ratings'
    id = db.Column(db.Integer(), primary_key=True)
    book_id = db.Column(db.Integer())
    user_id = db.Column(db.Integer())
    rating = db.Column(db.Integer())

    def __init__(self, user_id, book_id, rating):
        self.rating = rating
        self.book_id = book_id
        self.user_id = user_id

    def __repr__(self):
        return '<User Book Rate %r>' % self.rating