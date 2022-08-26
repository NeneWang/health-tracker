import datetime

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# --------- Database Models -----------#
class UserModel(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'{self.name} {self.user_id}'


class LogModel(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, primary_key=True, nullable=False)
    data = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Log | User ID : {self.user_id} | Date : {self.date}'


class SettingsModel(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'Setting | {self.user_id}'


# --------------- API --------------------#

# --------- User Resource -----------#
user_parser = reqparse.RequestParser()
user_parser.add_argument('user_id', type=int, required=True, help='User ID is required')
user_parser.add_argument('name', type=str, required=True, help='Username is required')
user_parser.add_argument('email', type=str, required=True, help='Email is required')
user_parser.add_argument('password', type=str, required=True, help='Password is required')

user_fields = {
    'user_id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'password': fields.String,
}


class User(Resource):
    def post(self):
        args = user_parser.parse_args()
        if login_user(args):
            return {'user_id': args['user_id']}
        return {'user_id': -1}

    # def get(self):
    #     args = user_parser.parse_args()
    #     user_model = UserModel.query.filter_by(user_id=args['user_id']).first()
    #

def login_user(args):
    user_model = UserModel.query.filter_by(user_id=args['user_id']).first()
    if not user_model:
        user_model = UserModel(user_id=args['user_id'], name=args['name'], email=args['email'], password=args['password'])
        db.session.add(user_model)
        db.session.commit()
    return authenticate_user(args, user_model)

def authenticate_user(args, user_model):
    has_correct_username = args['name'] == user_model.name
    has_correct_email = args['email'] == user_model.email
    has_correct_password = args['password'] == user_model.password
    return has_correct_password and has_correct_email and has_correct_username



# ----------- Log Resource ----------#
log_get_parser = reqparse.RequestParser()
log_get_parser.add_argument('user_id', type=int, required=True, help='Please provide User ID to get logs. ')

log_model_fields = {
    'user_id': fields.Integer,
    'date': fields.String,
    'data': fields.String,
}

log_post_parser = reqparse.RequestParser()
log_post_parser.add_argument('user_id', type=int, required=True, help='Please provide User ID to create log.')
log_post_parser.add_argument('date', type=str, required=True, help='Please provide DateTime to create log.')
log_post_parser.add_argument('data', type=str, required=True, help='Please provide Data to create log.')

class Log(Resource):
    # getAllLogs(user_id)
    @marshal_with(log_model_fields)
    def get(self):
        args = log_get_parser.parse_args()
        user_model = UserModel.query.filter_by(user_id=args['user_id']).first()
        if not user_model:
            abort(404, message=f'An user model related to ID: {args["user_id"]} is not found')

        log_models = LogModel.query.filter_by(user_id=args['user_id']).all()

        return log_models

    # createLog(date, user_id, data)
    def post(self):
        args = log_post_parser.parse_args()

        log_model = LogModel(user_id=args['user_id'], date=args['date'], data=args['data'])
        db.session.add(log_model)
        db.session.commit()

        return {'message': 'log created'}


# ----------- Settings Resource ----------#
settings_get_parser = reqparse.RequestParser()
settings_get_parser.add_argument('user_id', type=int, required=True, help='Please provide user ID to get settings')

settings_put_parser = reqparse.RequestParser()
settings_put_parser.add_argument('user_id', type=int, required=True, help='Please provide user ID')
settings_put_parser.add_argument('data', type=str, required=True, help='Please provide data')

setting_model_fields = {
    'user_id': fields.Integer,
    'data': fields.String
}

class Settings(Resource):
    # getSettings(user_id)
    @marshal_with(setting_model_fields)
    def get(self):
        args = settings_get_parser.parse_args()
        settings_model = SettingsModel.query.filter_by(user_id=args['user_id']).first()
        if not settings_model:
            abort(404, message=f'Setting related to this {args["id"]} is not found')
        return settings_model

    # updateSettings(user_id, data)
    @marshal_with(setting_model_fields)
    def put(self):
        args = settings_put_parser.parse_args()
        setting_model = SettingsModel.query.filter_by(user_id=args['user_id']).first()
        if not setting_model:
            self.post()
        for key in args.keys():
            setattr(setting_model, key, args[key])
            db.session.commit()
        return {'message': 'updated'}

    def post(self):
        args = settings_put_parser.parse_args()
        print(args)
        setting_model = SettingsModel(user_id=args['user_id'], data=args['data'])
        db.session.add(setting_model)
        db.session.commit()
        return {'message': 'created'}

api.add_resource(User, '/user')
api.add_resource(Log, '/log')
api.add_resource(Settings, '/settings')

# --------- Following Lines of code should only be executed if there is no Database created --------#
db.create_all()
# -------------------------#

if __name__ == '__main__':
    app.run()
