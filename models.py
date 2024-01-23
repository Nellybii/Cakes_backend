from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    __tablename__ ="user"

    id= db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(25), nullable=False)
    email=db.Column(db.String(25), nullable=False, unique=True)
    phone=db.Column(db.Integer, nullable=False, unique=True)
    password= db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"<User{self.username}, {self.email}>, {self.phone}"
    

# A user can have many addresses
# An address can have many users
class Address(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    Street_name=db.Column(db.String(25), nullable=False)
    Street_number=db.Column(db.Integer, nullable=False)
    region= db.Column(db.String(25), nullable=False)
    county= db.Column(db.String(25), nullable=False)


# Products
class Product(db.Model):
    __tablename__ ="product"
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(25), nullable=False)
    description=db.Column(db.String(25), nullable=False)
    category_id=db.Column(db.String(25), nullable=False)FK
    image=db.Column(db.String(25), nullable=False, unique=True)
    price=db.Column(db.Integer, nullable=False)

# Product Category
class ProductCategory(db.Model):
    __tablename__ ="product_category"
    id= db.Column(db.Integer, primary_key=True)
    category_name=db.Column(db.String(25), nullable=False)

#promotion- a promotion can have many categories
# a category can have many promotions
class Promotion(db.Model):
    __tablename__ ="promotion"
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(25), nullable=False)
    description=db.Column(db.String(25), nullable=False)
    discount_rate=db.Column(db.Integer, nullable=False)
    start_date=db.Column(db.TIMESTAMP, nullable=False)
    end_date=db.Column(db.TIMESTAMP, nullable=False)
    

# shopping cart
class ShoppingCart(db.Model):
    __tablename__ ="shopping_cart"
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, primary_key=True)


# Shopping cart not saved unless logged in
class ShoppingCartItem(db.Model):
    __tablename__ ="shopping_cart"
    id= db.Column(db.Integer, primary_key=True)
    cart_id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, primary_key=True)
    product_id= db.Column(db.Integer, primary_key=True)
    quantity=db.Column(db.Integer, primary_key=True)
  
class ShopOrder(db.Model):
    __tablename__='orders'

    id= db.Column(db.Integer, primary_key=True)
    customer_id=db.Column(db.Integer, db.ForeignKey("customers.id"))
    cake_id=db.Column(db.Integer, db.ForeignKey("cakes.id"))
    ordered_date=db.Column(db.TIMESTAMP, nullable=False)
    to_be_delivered_at=db.Column(db.TIMESTAMP, nullable=False)
    order_total = db.Column(db.Integer, primary_key=True)
    order_status=db.Column(db.String(25), nullable=False)
    cake=db.Relationship("Cake", back_populates='orders')
    customer=db.Relationship("Customer", back_populates='orders')
    deliver_address =db.Column(db.String(25), nullable=False)
    payment_method =  db.Column(db.String(25), nullable=False)

class OrderStatus(db.Model):
    __tablename__='order_status'
    id= db.Column(db.Integer, primary_key=True)
    status =  db.Column(db.String(25), nullable=False)



# An order has many products    
class order_line(db.Model):
    __tablename__ ="shopping_cart"
    id= db.Column(db.Integer, primary_key=True)
    product_id= db.Column(db.Integer, primary_key=True)
    order_id= db.Column(db.Integer, primary_key=True)
    quantity=db.Column(db.Integer, primary_key=True)
    price=db.Column(db.Integer, nullable=False)


# reviews
    
class UserReview(db.Model):
    __tablename__ ="user_review"
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, primary_key=True)
    order_id= db.Column(db.Integer, primary_key=True)
    rating= db.Column(db.Integer, primary_key=True)
    comment=db.Column(db.String(25), nullable=False, unique=True)




# class Customer(db.Model):
#     __tablename__='customers'

#     id= db.Column(db.Integer, primary_key=True)
#     name=db.Column(db.String(25), nullable=False)
#     phone=db.Column(db.Integer, nullable=False, unique=True)
#     location=db.Column(db.String(25), nullable=False)
#     quantity=db.Column(db.Integer, nullable=False)
#     order_id=db.Column(db.Integer, db.ForeignKey("orders.id"))
#     user_id=db.Column(db.Integer, db.ForeignKey("users.id"))

#     #relationships
#     cakes=db.Relationship('Cake', secondary="orders", back_populates='customers')
#     orders=db.Relationship('Order', back_populates='customers')


# class Cake(db.Model):
#     __tablename__= 'cakes'
#     id= db.Column(db.Integer, primary_key=True)
#     cake_flavour=db.Column(db.String, nullable=False)
#     size=db.Column(db.String, nullable=False)
#     order_category=db.Column(db.String, nullable=False)
#     order_id=db.Column(db.Integer, db.ForeignKey("orders.id"))

#     customers=db.Relationship('Customers', secondary="orders", back_populates='cakes')
#     orders=db.Relationship('Order', back_populates='cakes')

# class Order(db.Model):
#     __tablename__='orders'

#     id= db.Column(db.Integer, primary_key=True)
#     customer_id=db.Column(db.Integer, db.ForeignKey("customers.id"))
#     cake_id=db.Column(db.Integer, db.ForeignKey("cakes.id"))
#     ordered_at=db.Column(db.TIMESTAMP, nullable=False)
#     to_be_delivered_at=db.Column(db.TIMESTAMP, nullable=False)

#     cake=db.Relationship("Cake", back_populates='orders')
#     customer=db.Relationship("Customer", back_populates='orders')
  






