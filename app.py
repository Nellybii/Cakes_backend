from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import  Api
from models import db 

from routes.user import Register,Login

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS']= False
api = Api(app)

db.init_app(app)
migrate=Migrate(app, db)
bcrypt = Bcrypt()

api.add_resource(Register, '/register')
api.add_resource(Login, '/log')

if __name__=='__main__':
    app.run(debug=True)