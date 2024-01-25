from flask_restful import Resource, fields, reqparse, marshal_with, abort, request
from models import db, Promotion


promotion_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'discount_percentage': fields.Float,
    'start_date': fields.DateTime,
    'end_date':fields.DateTime,
   
}


class PromotionResource(Resource):
    promotion_parser = reqparse.RequestParser()
    promotion_parser.add_argument('name', type=str, help='Username is required', required=True)
    promotion_parser.add_argument('discount_percentage', type=str, help='Discount is required', required=True)
    promotion_parser.add_argument('start_date', type=str, help='Start date is required', required=True)
    promotion_parser.add_argument('end_date', type=str, help='End date is required', required=True)


    @marshal_with(promotion_fields)
    def get(self, id=None):
        if id:
            promotion = Promotion.query.get(id)
            if promotion is not None:
                return promotion
            else:
                abort(404, error="promotion not found")
        else:
            promotions = Promotion.query.all()
            return promotions


    def post(self):
        data = PromotionResource.promotion_parser.parse_args()
        existing_promotion = promotion.query.filter_by(name=data['name']).first()


        if existing_promotion:
            abort(400, error="Promotion with the same name already exists")


        promotion = promotion(**data)
        try:
            db.session.add(promotion)
            db.session.commit()
            return {"message": "created successfully"}, 201
        except:
            abort(500, error="Creation unsuccessful")


    def patch(self, id):
        data=request.json
        promotion=Promotion.query.filter_by(id=id).first()
        promotion.name=data['name']
        promotion.discount=data['discount_percentage']
        promotion.start_date=data['start_date']
        promotion.end_date_date=data['end_date']
       
        db.session.commit()
        return {"message":"updated successfully"}, 201


    def delete(self, id):
        promotion = Promotion.query.get(id)
        if promotion is None:
            abort(404, error="promotion not found")


        try:
            db.session.delete(promotion)
            db.session.commit()
            return {"message": f"promotion {id} deleted successfully"}
        except Exception as e:
            print(f"Error: {str(e)}")
            abort(500, error=f"Deletion for promotion {id} unsuccessful")


