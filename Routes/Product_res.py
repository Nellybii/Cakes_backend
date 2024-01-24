from flask_restful import Resource, fields, reqparse, marshal_with, abort, request
from models import db, Product

product_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'price': fields.String,
   
}

class ProductResource(Resource):
    product_parser = reqparse.RequestParser()
    product_parser.add_argument('name', type=str, help='Username is required', required=True)
    product_parser.add_argument('description', type=str, help='Phone is required', required=True)
    product_parser.add_argument('price', type=str, help='Price is required', required=True)
    # product_parser.add_argument('category', type=str, help='Password is required', required=True)

    @marshal_with(product_fields)
    def get(self, id=None):
        if id:
            product = Product.query.get(id)
            if product is not None:
                return product
            else:
                abort(404, error="Product not found")
        else:
            products = Product.query.all()
            return products

    def post(self):
        data = ProductResource.product_parser.parse_args()
        existing_product = Product.query.filter_by(name=data['name']).first()

        if existing_product:
            abort(400, error="Product with the same name already exists")

        product = Product(**data)
        try:
            db.session.add(product)
            db.session.commit()
            return {"message": "created successfully"}, 201
        except:
            abort(500, error="Creation unsuccessful")

    def patch(self, id):
        data=request.json
        product=Product.query.filter_by(id=id).first()
        product.name=data['name']
        product.description=data['description']
        product.price=data['price']
        db.session.commit()
        return {"message":"updated successfully"}, 201

    def delete(self, id):
        product = Product.query.get(id)
        if product is None:
            abort(404, error="Product not found")

        try:
            db.session.delete(product)
            db.session.commit()
            return {"message": f"Product {id} deleted successfully"}
        except Exception as e:
            print(f"Error: {str(e)}")
            abort(500, error=f"Deletion for Product {id} unsuccessful")
