from flask import request
from flask_restful import Resource
from models import db, ShoppingCartItem


class ShoppingCartItemsResource(Resource):
    def get(self):
        shopping_cart_items = ShoppingCartItem.query.all()
        shopping_cart_data = [
            {
                "id": item.id,
                "cart_id": item.cart_id,
                "product_id": item.product_id,
                "quantity": item.quantity
            }
            for item in shopping_cart_items
        ]
        return shopping_cart_data
    
    def post(self):
        data = request.get_json()
        cart_id = data.get("cart_id")
        product_id = data.get("product_id")
        quantity = data.get("quantity")


        if not all([cart_id, product_id, quantity]):
            return {"errors": ["validation errors"]}, 400


        shopping_cart_item = ShoppingCartItem(
            cart_id=cart_id,
            product_id=product_id,
            quantity=quantity
        )


        db.session.add(shopping_cart_item)
        db.session.commit()


        return {
            "id": shopping_cart_item.id,
            "cart_id": shopping_cart_item.cart_id,
            "product_id": shopping_cart_item.product_id,
            "quantity": shopping_cart_item.quantity
        }



class ShoppingCartItemResource(Resource):
    def get(self, item_id):
        item = ShoppingCartItem.query.get(item_id)


        if item:
            item_data = {
                "id": item.id,
                "cart_id": item.cart_id,
                "product_id": item.product_id,
                "quantity": item.quantity
            }
            return item_data
        else:
            return {"error": "Shopping cart item not found"}, 404


    
    def put(self, item_id):
        item = ShoppingCartItem.query.get(item_id)


        if not item:
            return {"error": "Shopping cart item not found"}, 404


        data = request.get_json()
        item.cart_id = data.get("cart_id", item.cart_id)
        item.product_id = data.get("product_id", item.product_id)
        item.quantity = data.get("quantity", item.quantity)


        db.session.commit()


        updated_item_data = {
            "id": item.id,
            "cart_id": item.cart_id,
            "product_id": item.product_id,
            "quantity": item.quantity
        }


        return updated_item_data


    def delete(self, item_id):
        item = ShoppingCartItem.query.get(item_id)


        if item:
            db.session.delete(item)
            db.session.commit()
            return {}, 204
        else:
            return {"error": "Shopping cart item not found"}, 404
