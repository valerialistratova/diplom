# -*- coding: utf-8 -*-
from project import app
from project import db
from datetime import datetime
from collections import OrderedDict
from sqlalchemy import func, not_
from project.models import Users, Books, Devices, Log, BooksUsers, UsersBooksRatings
from flask import render_template, request, jsonify, send_file, session, redirect, url_for
# from flask.ext.wtf import Form, TextField, validators
# from math import sqrt
import hashlib



#### controllers

# @app.route('/', methods=['POST', 'GET'])
# def hello_world():
#     content = request.get_json()
#     res = jsonify(device_id=content['device_id'])
#     print('device_id ' + str(content['device_id']))
#     print('progress ' + str(content['progress']))
#     # print('scroll_y ' + str(content['scroll_y']))
#     # print('screen height ' + str(content['height']))
#     # print('total_height' + str(content['total_height']))
#     print('book_name ' + str(content['book_name']))
#     print('text_length ' + str(content['text_length']))
#     user = UserPwd.query.limit(1).all()
#     print user
#     return res

@app.route('/')
def index():
    user = Users.Users.query.get(session['user_id'])
    counters = get_counters()

    return render_template('main/index.html', user=user, counters=counters)


@app.route('/history', methods=['POST'])
def history():
    if is_logged():
        books = get_monthly_history()

        return render_template('main/history.html', books=books)
    else:
        return redirect(url_for('login'))


@app.route('/people', methods=['POST'])
def people():
    return 'Under construction - people:)'


@app.route('/bookmarks', methods=['POST'])
def bookmarks():
    if is_logged():
        books = get_bookmarked()
        return render_template('main/bookmarks.html', books=books)
    else:
        return redirect(url_for('login'))



@app.route('/recommendation', methods=['POST'])
def recommendation():
    if is_logged():
        books = get_recommended()

        return render_template('main/recommendation.html', books=books)
    else:
        return redirect(url_for('login'))


@app.route('/get-client-data', methods=['POST'])
def get_client_data():
    link = url_for('login-with-id', uid=1, _external=True)
    secret_key = ''
    res = jsonify(link=link, secret_key=secret_key)
    print res

    return res


@app.route('/login-android', methods=['POST'])
def loginAndroid(uid=None):
    error = None
    uid = request.form['email']
    if valid_login(uid, request.form['password'], True):
        current_user = Users.Users.query.filter_by(email=uid).first()
        return jsonify(userId=current_user.user_id,success=True)
    else:
        return jsonify(success=False)



@app.route('/save-progress-android', methods=['POST'])
def saveProgressAndroid():
    book_id = request.form['book_id']
    device_id = request.form['device_id']
    datetime = request.form['datetime']
    progress = request.form['progress']

    log = Log.Log(device_id, book_id, datetime, progress)

    db.session.add(log)
    db.session.commit()
    return jsonify(success=True)


@app.route('/login', methods=['POST', 'GET'])
@app.route('/login/<int:uid>', endpoint='login-with-id')
def login(uid=None):
    error = None
    if request.method == 'POST':
        print 'POST'
        by_email = True
        uid = request.form['email']
        if valid_login(uid, request.form['password'], by_email):
            return log_user_in()
        else:
            error = True

    return render_template('main/login.html', id=uid, error=error)


@app.route('/logout')
def logout():
    session['user_id'] = None
    return redirect(url_for('login'))


@app.route('/get_image/<category>/<filename>')
def get_image(category, filename):
    if category == 'user':
        filename = 'uploads/userpics/' + filename

    if category == 'book':
        filename = 'uploads/books/' + filename

    return send_file(filename, mimetype='image/jpeg,image/png')


@app.route('/get-counters', methods=['POST'])
def retrieve_counters():
    counters = get_counters()
    return jsonify(counters)


@app.errorhandler(404)
def not_found(error):
    return error
    return render_template('error.html'), 404


@app.route('/save-rate', methods=['POST'])
def save_rate():
    if is_logged():
        rated = UsersBooksRatings.UsersBooksRatings.query\
            .filter(UsersBooksRatings.UsersBooksRatings.user_id == session['user_id'])\
            .filter(UsersBooksRatings.UsersBooksRatings.book_id == request.form['book_id']).first()

        if rated is not None:
            rated.rating = request.form['rate']
        else:
            rated = UsersBooksRatings.UsersBooksRatings(session['user_id'], request.form['book_id'], request.form['rate'])


        db.session.add(rated)
        db.session.commit()
        return jsonify(ratedId=rated.id)
    else:
        return 'NOT LOGGED', 501


@app.route('/save-fav', methods=['POST'])
def save_favorite():
    if is_logged():
        faved_id = None
        if request.form['is_liked'] == 'true':
            faved = BooksUsers.BooksUsers(request.form['book_id'], session['user_id'])
            db.session.add(faved)
            db.session.commit()
            faved_id = faved.id
        elif request.form['faved_id'] > 0:
            faved = BooksUsers.BooksUsers.query.get(request.form['faved_id'])
            db.session.delete(faved)
            db.session.commit()

        return jsonify(favedId=faved_id)
    return 'NOT LOGGED', 501


#### End of controllers


def get_monthly_history():
    """
        gets monthly history of reading for current user
        returns dictionary:
        dict('month-year'=[dict(Books.Books), ...], ...)
    """

    min_progress = 5
    max_progress = 98

    current_user_books = get_read_books()

    subquery_start = (db.session.query(
                      Log.Log.book_id,
                      Log.Log.datetime.label('start')
    ).filter(Log.Log.progress <= min_progress)
     .group_by(Log.Log.book_id).order_by(Log.Log.progress)
    ).subquery()

    subquery_finish = (db.session.query(
                       Log.Log.book_id,
                       Log.Log.datetime.label('finish')
    ).filter(Log.Log.progress >= max_progress)
     .group_by(Log.Log.book_id).order_by(Log.Log.progress.desc())
    ).subquery()

    subquery_progress = (db.session.query(
                         Log.Log.book_id,
                         (func.max(Log.Log.progress).label('progress'))
    ).group_by(Log.Log.book_id)
    ).subquery()

    subquery_rating = (db.session.query(
                       UsersBooksRatings.UsersBooksRatings.book_id.label('book_id'),
                       UsersBooksRatings.UsersBooksRatings.rating.label('rating')
    ).filter(UsersBooksRatings.UsersBooksRatings.user_id == session['user_id'])
    ).subquery()

    detailed_books_list = OrderedDict()
    for book in current_user_books:

        book = (db.session.query(Books.Books,
                                 subquery_start.c.start,
                                 subquery_finish.c.finish,
                                 subquery_progress.c.progress,
                                 subquery_rating.c.rating)
                  .outerjoin(subquery_start, (Books.Books.book_id == subquery_start.c.book_id))
                  .outerjoin(subquery_finish, (Books.Books.book_id == subquery_finish.c.book_id))
                  .outerjoin(subquery_progress, (Books.Books.book_id == subquery_progress.c.book_id))
                  .outerjoin(subquery_rating, (Books.Books.book_id == subquery_rating.c.book_id))
                  .filter(Books.Books.book_id == book.book_id)).first()

        print book.keys()

        newBook = {'Books': book.Books, 'progress': book.progress, 'start': book.start, 'finish': book.finish, 'rating': book.rating}

        if book.start:
            key = book.start.strftime("%B, %Y")
            newBook['start'] = book.start.strftime('%d %B').decode('1251')

        if book.finish:
            newBook['finish'] = book.finish.strftime('%d %B').decode('1251')

        if key not in detailed_books_list:
            detailed_books_list[key] = []

        detailed_books_list[key].append(book)

    return detailed_books_list


def get_read_books(user_id=None):
    date = subtract_years(datetime.now(), 1)

    if user_id is None:
        user_id = session['user_id']

    books = Log.Log.query\
                .filter(Log.Log.device_id == user_id,  Log.Log.datetime >= date,
                        Log.Log.progress <= 10)\
                .group_by(Log.Log.book_id)\
                .order_by(Log.Log.datetime.desc())\
                .all()

    return books


def get_recommended():

    # print calculate_similar_items(get_data_for_recommendations())

    subquery_faved = (db.session.query(
                      BooksUsers.BooksUsers.id.label('faved_id'),
                      BooksUsers.BooksUsers.bookmarked_id.label('bookmarked_id')
    ).filter(BooksUsers.BooksUsers.user_id == session['user_id'])).subquery()

    user_books = get_read_books()
    user_books_ids = []
    for book in user_books:
        user_books_ids.append(book.book_id)

    books = (db.session.query(Books.Books,
                              subquery_faved.c.faved_id)
                  .outerjoin(subquery_faved, (Books.Books.book_id == subquery_faved.c.bookmarked_id))
                  .filter(not_(Books.Books.book_id.in_(user_books_ids)))
                  .group_by(Books.Books.book_id)).all()

    return books


def get_user_rates(user_id):
    rates = UsersBooksRatings.UsersBooksRatings.query.filter(UsersBooksRatings.UsersBooksRatings.user_id == user_id).all()
    return rates


def get_bookmarked():

    subquery_faved = (db.session.query(
                      BooksUsers.BooksUsers.id.label('faved_id'),
                      BooksUsers.BooksUsers.bookmarked_id.label('bookmarked_id')
    ).filter(BooksUsers.BooksUsers.user_id == session['user_id'])).subquery()


    books = (db.session.query(Books.Books,
                              subquery_faved.c.faved_id)
                  .join(subquery_faved, (Books.Books.book_id == subquery_faved.c.bookmarked_id))
                  .group_by(Books.Books.book_id)).all()

    return books


def valid_login(uid, password, by_email):
    if by_email:
        current_user = Users.Users.query.filter_by(email=uid).first()
    else:
        current_user = Users.Users.query.get(uid)

    if current_user.password == password:
        session['user_id'] = current_user.user_id

        return True
    else:
        return False


def log_user_in():
    print 'log user in'
    return redirect(url_for('index'))


def subtract_years(dt, years):
    try:
        dt = dt.replace(year=dt.year-years)
    except ValueError:
        dt = dt.replace(year=dt.year-years, day=dt.day-1)
    return dt

def is_logged():
    return session['user_id'] is not None


def prepare_password(password):
    return hashlib.md5(password).hexdigest()


def get_counters():
    counters = dict(
        bookmarks=len(get_bookmarked()),
        recommended=len(get_recommended()),
        history=len(get_read_books())
    )

    return counters


def get_data_for_recommendations():
    all_users_data = Users.Users.query.all()
    all_rates = dict()

    for user in all_users_data:
        all_rates[user.user_id] = prepare_rates(get_user_rates(user.user_id))

    return all_rates


def prepare_rates(rates):
    user_rates = dict()
    for rate in rates:
        user_rates[rate.book_id] = rate.rating

    return user_rates


# Возвращает оценку подобия book1 и book2 на основе расстояния
def sim_distance(prefs, book1, book2):
    # Получить список предметов, оцененных обоими
    si = {}
    for item in prefs[book1]:
        if item in prefs[book2]:
            si[item] = 1
    # Если нет ни одной общей оценки, вернуть 0
    if len(si) == 0:
        return 0
    # Сложить квадраты разностей
    sum_of_squares = sum([pow(prefs[book1][item] - prefs[book2][item], 2)
                          for item in prefs[book1] if item in prefs[book2]])
    return 1 / (1 + sum_of_squares)


def transform_prefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
    # Обменять местами человека и книгу
    result[item][person] = prefs[person][item]
    return result


def calculate_similar_items(prefs, n=10):
    # Создать словарь, содержащий для каждого образца те образцы, которые
    # больше всего похожи на него.
    result = {}
    # Обратить матрицу предпочтений, чтобы строки соответствовали образцам
    item_prefs = transform_prefs(prefs)
    c = 0
    for item in item_prefs:
        # Обновление состояния для больших наборов данных
        c += 1
        if c % 100 == 0:
            print "%d / %d" % (c, len(item_prefs))

    # Найти образцы, максимально похожие на данный
    scores = top_matches(item_prefs, item, n=n, similarity=sim_distance)
    result[item] = scores
    return result


def top_matches(prefs, person, n=5, similarity=None):
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]
    # Отсортировать список по убыванию оценок
    scores.sort()
    scores.reverse()
    return scores[0:n]




