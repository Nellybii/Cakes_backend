from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    __tablename__ ="users"

    id= db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(25), nullable=False)
    email=db.Column(db.String(25), nullable=False, unique=True)
    phone=db.Column(db.Integer, nullable=False, unique=True)
    profile_picture=db.Column(db.VARCHAR, nullable=False)
    password= db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"<User{self.username}, {self.email}>"

class Customer(db.Model):
    __tablename__='customers'

    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(25), nullable=False)
    phone=db.Column(db.Integer, nullable=False, unique=True)
    location=db.Column(db.String(25), nullable=False)
    quantity=db.Column(db.Integer, nullable=False)
    order_id=db.Column(db.Integer, db.ForeignKey("order.id"))
    user_id=db.Column(db.Integer, db.ForeignKey("user.id"))

    #relationships
    cakes=db.Relationship('Cake', secondary="orders", back_populates='customers')
    orders=db.Relationship('Order', back_populates='customers')

class Order(db.Model):
    __tablename__='orders'

    id= db.Column(db.Integer, primary_key=True)
    customer_id=db.Column(db.Integer, db.ForeignKey("customer.id"))
    cake_id=db.Column(db.Integer, db.ForeignKey("cake.id"))
    ordered_at=db.Column(db.TIMESTAMP, nullable=False)
    to_be_delivered_at=db.Column(db.TIMESTAMP, nullable=False)

    cake=db.Relationship("Cake", back_populates='orders')
    customer=db.Relationship("Customer", back_populates='orders')

class Cake(db.Model):
    __tablename__= 'cakes'
    id= db.Column(db.Integer, primary_key=True)
    cake_flavour=db.Column(db.String, nullable=False)
    size=db.Column(db.String, nullable=False)
    order_category=db.Column(db.String, nullable=False)
    order_id=db.Column(db.Integer, db.ForeignKey("order.id"))

    customers=db.Relationship('Customers', secondary="orders", back_populates='cakes')
    orders=db.Relationship('Order', back_populates='cakes')

  






