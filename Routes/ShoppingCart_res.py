from flask_restful import Resource, fields, reqparse, marshal_with, abort, request
from models import db, ShoppingCart

cart_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'items': fields.String,
}

class ShoppingCartResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user', type=str, help='User is required', required=True)
    parser.add_argument('items', type=str, help='Items is required', required=True)
    
    

    @marshal_with(cart_fields)
    def get(self, id=None):
        if id:
            cart = ShoppingCart.query.filter_by(id=id).filter()
            if cart is not None:
                return cart
            else:
                abort(404, error="Order not found")
        else:
            carts = ShoppingCart.query.all()
            return carts

    def post(self):
        data = ShoppingCartResource.parser.parse_args()
        cart = ShoppingCart(**data)
        try:
            db.session.add(cart)
            db.session.commit()
            return {"message":"created successfully"}, 200
        except:
            abort(500, error="Creation unsuccessful")

    def patch(self, id):
        data=request.json
        cart=ShoppingCart.query.filter_by(id=id).first()
        cart.user=data['user']
        cart.items=data['items']
        db.session.commit()
        return {"message":"updated successfully"}, 201


    def delete(self, id):
        cart = ShoppingCart.query.get(id)
        if cart is None:
            abort(404, error="Product not found")

        try:
            db.session.delete(cart)
            db.session.commit()
            return {"message": f"Cart {id} deleted successfully"}
        except Exception as e:
            print(f"Error: {str(e)}")
            abort(500, error=f"Deletion for cart {id} unsuccessful")
