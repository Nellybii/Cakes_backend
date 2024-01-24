from flask_restful import Resource, fields, abort, reqparse, marshal_with
from flask_bcrypt import generate_password_hash, check_password_hash

from models import db, User

user_fields={
    "id":fields.Integer,
    "username":fields.String,
    "email":fields.String,
    "password":fields.String,
    "phone":fields.Integer
    # "addresses":fields.String,
}

class SignupResource(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username', help='Username is required', required=True)
    parser.add_argument('email', help='Email is required', required=True)
    parser.add_argument('password', help='Password is required', required=True)
    # parser.add_argument('addresses', help='Address is required', required=True)
    

    @marshal_with(user_fields)
    def get(self, id=None):
        if id:
            user=User.query.filter_by(id=id).first()
            if user is not None:
                return user
            else:
                abort(401, error="User {id} do not exist")
        else:
            users=User.query.all()
            return users
        
    def post(self):
        data=SignupResource.parser.parse_args()
        data['password']=generate_password_hash(data['password'])
        user=User(**data)

        email=User.query.filter_by(email=data['email']).one_or_none()
        if email:
            return "Email exists"

        try:
            db.session.add(user)
            db.session.commit()
            return {"message":"User created successfully"}
        except:
            return{"message": "Creation unsuccessful"}, 201
        
class LoginResource(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('email', required= True, help= "Email is required")
    parser.add_argument('password', required= True, help= "Password is required")

    def post(self):
        data=LoginResource.parser.parse_args()

        user =User.query.filter_by(email= data['email']).first()

        if user:
            is_password_correct = check_password_hash(user.password, data['password'])

            if is_password_correct:
        
                return {"message": "login successful", "status":"success"}, 200
            
            else:
               return {"message": "invalid email/password", "status":"fail"}, 403

        return {"message": "invalid email/password", "status":"fail"}, 403
    
    