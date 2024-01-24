from flask import request
from flask_restful import Resource
from models import db, Address, User


class AddressesResource(Resource):
    def get(self):
        addresses = Address.query.all()
        address_data = [
            {
                "id": address.id,
                "Street_name": address.Street_name,
                "Street_number": address.Street_number,
                "region": address.region,
                "county": address.county,
                "user_id": address.user_id
            }
            for address in addresses
        ]
        return address_data

    def post(self):
        data = request.get_json()
        user_id = data.get("user_id")
        street_name = data.get("Street_name")
        street_number = data.get("Street_number")
        region = data.get("region")
        county = data.get("county")


        if not all([user_id, street_name, street_number, region, county]):
            return {"errors": ["validation errors"]}, 400


        user = User.query.get(user_id)


        if not user:
            return {"errors": ["User not found"]}, 400


        address = Address(
            Street_name=street_name,
            Street_number=street_number,
            region=region,
            county=county,
            user=user
        )


        db.session.add(address)
        db.session.commit()


        return {
            "id": address.id,
            "Street_name": address.Street_name,
            "Street_number": address.Street_number,
            "region": address.region,
            "county": address.county,
            "user_id": address.user_id
        }

class AddressResource(Resource):
    def get(self, address_id):
        address = Address.query.get(address_id)


        if address:
            address_data = {
                "id": address.id,
                "Street_name": address.Street_name,
                "Street_number": address.Street_number,
                "region": address.region,
                "county": address.county,
                "user_id": address.user_id
            }
            return address_data
        else:
            return {"error": "Address not found"}, 404


    def put(self, address_id):
        address = Address.query.get(address_id)


        if not address:
            return {"error": "Address not found"}, 404


        data = request.get_json()
        address.Street_name = data.get("Street_name", address.Street_name)
        address.Street_number = data.get("Street_number", address.Street_number)
        address.region = data.get("region", address.region)
        address.county = data.get("county", address.county)


        db.session.commit()


        updated_address_data = {
            "id": address.id,
            "Street_name": address.Street_name,
            "Street_number": address.Street_number,
            "region": address.region,
            "county": address.county,
            "user_id": address.user_id
        }


        return updated_address_data


    def delete(self, address_id):
        address = Address.query.get(address_id)


        if address:
            db.session.delete(address)
            db.session.commit()
            return {}, 204
        else:
            return {"error": "Address not found"}, 404
