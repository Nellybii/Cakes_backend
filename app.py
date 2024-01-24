from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db 
from Routes.Address_res import AddressResource
from Routes.CartItem__res import ShoppingCartItemResource
from Routes.ProductCategory import ProductCategoryResource  


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db.init_app(app)
migrate=Migrate(app, db)
api=Api(app)

@app.route('/')
def index():
    return "Hello World!"

api.add_resource(AddressResource, '/addresses', '/addresses/<int:address_id>')
api.add_resource(ShoppingCartItemResource, '/shopping_cart_items', '/shopping_cart_items/<int:item_id>')
api.add_resource(ProductCategoryResource, '/product_categories')





if __name__=='__main__':
    app.run(port=5555)