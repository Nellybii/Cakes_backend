from flask_restful import Resource, fields, reqparse, marshal_with, abort, request
from models import db, Order, OrderItem

order_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'order_date': fields.String,
    'order_items': fields.List(fields.Nested({
        "id":fields.Integer,
        "quantity":fields.Integer,
        "product_id":fields.Integer
    })),
   
}

class OrderResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user', type=str, help='User is required', required=True)
    parser.add_argument('order_date', type=str, help='Order is required', required=True)
    parser.add_argument('Order_items', type=str, help='Order items is required', required=True)
    

    @marshal_with(order_fields)
    def get(self, id=None):
        if id:
            order = Order.query.filter_by(id=id).filter()
            if order is not None:
                return order
            else:
                abort(404, error="Order not found")
        else:
            orders = Order.query.all()
            return orders

    def post(self):
        data = OrderResource.parser.parse_args()
        order = Order(**data)
        try:
            db.session.add(order)
            db.session.commit()
            return {"message":"created successfully"}, 200
        except:
            abort(500, error="Creation unsuccessful")

    def patch(self, id):
        data = request.json
        order = Order.query.filter_by(id=id).first()
        
        if not order:
            abort(404, error="Order not found")

        order.user = data.get('user', order.user)  
        order.order_date = data.get('order_date', order.order_date) 
        order_items_data = data.get('order_items', [])

        order.order_items = [
            OrderItem(quantity=item['quantity'], product_id=item['product_id'])
            for item in order_items_data
        ]

        try:
            db.session.commit()
            return {"message": "updated successfully"}, 201
        except Exception as e:
            print(f"Error: {str(e)}")
            db.session.rollback()
            abort(500, error="Update unsuccessful")


    def delete(self, id):
        order = Order.query.get(id)
        if order is None:
            abort(404, error="Product not found")

        try:
            db.session.delete(Order)
            db.session.commit()
            return {"message": f"Order {id} deleted successfully"}
        except Exception as e:
            print(f"Error: {str(e)}")
            abort(500, error=f"Deletion for Order {id} unsuccessful")
