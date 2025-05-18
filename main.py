import flask
from flask import Flask, jsonify, make_response, request
from flask_restful import Api

from data import db_session
from data.users import User

app = Flask(__name__)
api = Api(app)

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('id', 'name',
                                    'surname', 'age', 'position', 'speciality', 'address', 'email',
                                    'hashed_password', 'modified_date'))
                 for item in news]
        }
    )


@blueprint.route('/api/user/<int:user_id>', methods=['GET'])
def get_new(user_id):
    print(type(user_id))
    if type(user_id) != int:
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    news = db_sess.query(User).all()
    flag = []
    for r in news:
        flag.append(r.id)
    if user_id not in flag:
        return make_response(jsonify({'error': 'Bad request'}), 400)
    news = db_sess.query(User).get(user_id)
    return jsonify(
        {
            'user':
                [news.to_dict(only=('id', 'name',
                                    'surname', 'age', 'position', 'speciality', 'address', 'email',
                                    'hashed_password', 'modified_date'))]
        }
    )


@blueprint.route('/api/user/post', methods=['POST'])
def create_news():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['id', 'name',
                  'surname', 'age', 'position', 'speciality', 'address', 'email',
                  'hashed_password', 'modified_date']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    news = User(
        id=request.json['id'],
        name=request.json['name'],
        surname=request.json['surname'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email'],
        hashed_password=request.json['hashed_password'],
        modified_date=request.json['modified_date']
    )
    db_sess.add(news)
    db_sess.commit()
    return jsonify({'id': news.id})


@blueprint.route('/api/user/del/<int:user_id>', methods=['DELETE'])
def delete_news(user_id):
    if not user_id:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    db_sess = db_session.create_session()
    news = db_sess.query(User).get(user_id)
    if not news:
        return make_response(jsonify({'error': 'Bad request'}), 404)
    db_sess.delete(news)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/user/red', methods=['POST'])
def redact_news():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['id', 'name',
                  'surname', 'age', 'position', 'speciality', 'address', 'email',
                  'hashed_password', 'modified_date']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    if not request.json['id']:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    db_sess = db_session.create_session()
    news = db_sess.query(User).get(request.json['id'])
    if not news:
        return make_response(jsonify({'error': 'Bad request'}), 404)
    db_sess.delete(news)
    db_sess.commit()
    db_sess = db_session.create_session()
    news = User(
        id=request.json['id'],
        name=request.json['name'],
        surname=request.json['surname'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email'],
        hashed_password=request.json['hashed_password'],
        modified_date=request.json['modified_date']
    )
    db_sess.add(news)
    db_sess.commit()
    return jsonify({'id': news.id})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


def main():
    db_session.global_init("db/db.db")
    app.register_blueprint(blueprint)
    app.run()
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
