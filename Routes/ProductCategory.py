from flask import request
from flask_restful import Resource
from models import db, ProductCategory


class ProductCategoryResource(Resource):
    def get(self):
        categories = ProductCategory.query.all()
        category_data = [
            {
                "id": category.id,
                "cname": category.name
            }
            for category in categories
        ]
        return category_data


    def post(self):
        data = request.get_json()
        category_name = data.get("name")


        if not category_name:
            return {"errors": ["validation errors"]}, 400


        new_category = ProductCategory(name=category_name)


        db.session.add(new_category)
        db.session.commit()


        return {
            "id": new_category.id,
            "name": new_category.name
        }, 201



