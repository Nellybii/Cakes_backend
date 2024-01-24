from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db 
from Routes.Address_res import AddressesResource, AddressResource
from Routes.CartItem__res import ShoppingCartItemResource, ShoppingCartItemsResource
from Routes.ProductCategory import ProductCategoryResource
from Routes.Product_res import ProductResource
from Routes.Order_res import OrderResource
from Routes.ShoppingCart_res import ShoppingCartResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)


# Resources
api.add_resource(AddressesResource, '/addresses')
api.add_resource(AddressResource, '/addresses/<int:address_id>')
api.add_resource(ShoppingCartItemsResource, '/shopping_cart_items')
api.add_resource(ShoppingCartItemResource, '/shopping_cart_items/<int:item_id>')
api.add_resource(ProductCategoryResource, '/product_categories')
api.add_resource(ProductResource, '/products', '/products/<int:id>')
api.add_resource(OrderResource, '/orders', '/orders/<int:id>')
api.add_resource(ShoppingCartResource, '/carts', '/carts/<int:id>')

if __name__ == '__main__':
    app.run(port=5555)
