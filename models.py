from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db=SQLAlchemy()

class User(db.Model):
    __tablename__ ="user"

    id= db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(25), nullable=False)
    email=db.Column(db.String(25), nullable=False, unique=True)
    phone=db.Column(db.String(25), nullable=False, unique=True)
    password= db.Column(db.String(100), nullable=False)
     #timestamp
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now() ,default=func.now())
   
    def __repr__(self):
        return f"<User{self.username}, {self.email}>, {self.phone}"


# A user can have many addresses
# An address can have many users
class Address(db.Model):
    __tablename__ ="address"
    id= db.Column(db.Integer, primary_key=True)
    street_name=db.Column(db.String(25), nullable=False)
    street_number=db.Column(db.Integer, nullable=False)
    region= db.Column(db.String(25), nullable=False)
    county= db.Column(db.String(25), nullable=False)
    # relationships
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # relationships
    users = db.relationship('User', backref='address', lazy=True)
    #Multiple users can have the same address
    def __repr__(self):
        return f"{self.Street_name}, {self.Street_number}>, {self.region},{self.county}>"
    

# Products
# class Product(db.Model):
#     __tablename__ ="product"
#     id= db.Column(db.Integer, primary_key=True)
#     name=db.Column(db.String(25), nullable=False)
#     description=db.Column(db.Text, nullable=False)
#     category_id=db.Column(db.Integer, db.ForeignKey('product_category.id'),
#         nullable=False)
#     image=db.Column(db.String(25), nullable=False)
#     price=db.Column(db.Integer, nullable=False)

#      # relationships
#     category = db.relationship('ProductCategory', backref='product', lazy=True)

#     def __repr__(self):
#         return f"{self.name}, {self.description}>, {self.price}"

# # Product Category
# class ProductCategory(db.Model):
#     __tablename__ ="product_category"
#     id= db.Column(db.Integer, primary_key=True)
#     category_name=db.Column(db.String(25), nullable=False)


#     def __repr__(self):
#         return f"{self.category_name}"

# #promotion- a promotion can have many categories
# # a category can have many promotions
# class Promotion(db.Model):
#     __tablename__ ="promotion"
#     id= db.Column(db.Integer, primary_key=True)
#     name=db.Column(db.String(25), nullable=False)
#     description=db.Column(db.Text, nullable=False)
#     discount_rate=db.Column(db.Integer, nullable=False)
#     start_date=db.Column(db.TIMESTAMP, nullable=False)
#     end_date=db.Column(db.TIMESTAMP, nullable=False)


#     def __repr__(self):
#         return f"{self.name}, {self.description}>, {self.discount_rate}"
    

# # shopping cart
# class ShoppingCart(db.Model):
#     __tablename__ ="shopping_cart"
#     id= db.Column(db.Integer, primary_key=True)
#     user_id= db.Column(db.Integer, db.ForeignKey('user.id'),
#         nullable=False)

#     def __repr__(self):
#         return f"{self.user_id}"

# # Shopping cart not saved unless logged in
# class ShoppingCartItem(db.Model):
#     __tablename__ ="shopping_cart_item"
#     id= db.Column(db.Integer, primary_key=True)
#     cart_id= db.Column(db.Integer, db.ForeignKey('shopping_cart.id'),
#         nullable=False)
#     user_id= db.Column(db.Integer, db.ForeignKey('user.id'),
#         nullable=False)
#     product_id= db.Column(db.Integer, db.ForeignKey('product.id'),
#         nullable=False)
#     quantity=db.Column(db.Integer, primary_key=True)

#     def __repr__(self):
#         return f"{self.user_id}, {self.quantity}"
  
# class ShopOrder(db.Model):
#     __tablename__='orders'

#     id= db.Column(db.Integer, primary_key=True)
#     customer_id=db.Column(db.Integer, db.ForeignKey("user.id"))
#     order_id=db.Column(db.Integer, db.ForeignKey('shopping_cart.id'),
#         nullable=False)
#     ordered_date=db.Column(db.TIMESTAMP, nullable=False)
#     to_be_delivered_at=db.Column(db.TIMESTAMP, nullable=False)
#     order_total = db.Column(db.Integer, primary_key=True)
#     order_status=db.Column(db.String(25), nullable=False)
   
#     customer=db.Relationship("Customer", back_populates='orders')
#     deliver_address =db.Column(db.String(25), nullable=False)
#     payment_method =  db.Column(db.String(25), nullable=False)


#     def __repr__(self):
#         return f"<User{self.customer_id}, {self.email}>, {self.phone}"

# class OrderStatus(db.Model):
#     __tablename__='order_status'
#     id= db.Column(db.Integer, primary_key=True)
#     status =  db.Column(db.String(50), nullable=False)

#     def __repr__(self):
#         return f"{self.status}"



# # An order has many products    
# class order_line(db.Model):
#     __tablename__ ="order_line"
#     id= db.Column(db.Integer, primary_key=True)
#     product_id= db.Column(db.Integer, db.ForeignKey('product.id'),
#         nullable=False)
#     order_id=db.Column(db.Integer, db.ForeignKey('product.id'),
#         nullable=False)
#     quantity=db.Column(db.Integer, primary_key=True)
#     price=db.Column(db.Integer, nullable=False)


#     def __repr__(self):
#         return f"{self.username}, {self.email}>, {self.phone}"

# # reviews
    
# class UserReview(db.Model):
#     __tablename__ ="user_review"
#     id= db.Column(db.Integer, primary_key=True)
#     user_id= db.Column(db.Integer, db.ForeignKey('user.id'),
#         nullable=False)
#     product_id= db.Column(db.Integer, db.ForeignKey('product.id'),
#         nullable=False)
#     rating= db.Column(db.Integer, primary_key=True)
#     comment=db.Column(db.Text, nullable=False)

#     def __repr__(self):
#         return f"{self.order_id}, {self.comment}>, {self.rating}"




