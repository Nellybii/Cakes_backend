from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    __tablename__ ="users"

    id= db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(25), nullable=False)
    email=db.Column(db.String(25), nullable=False, unique=True)
    phone=db.Column(db.String(25), nullable=False, unique=True)
    password= db.Column(db.String(100), nullable=False)

    # relationships
    addresses = db.relationship('Address', backref='users', lazy=True)
    orders=db.relationship("ShopOrder", backref="users", lazy=True)

    #timestamp
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), nullable=False)



    def __repr__(self):
        return f"<User{self.username}, {self.email}>, {self.phone}"
    

# A user can have many addresses
# An address can have many users
class Address(db.Model):
    __tablename__ ="addresses"
    id= db.Column(db.Integer, primary_key=True)
    Street_name=db.Column(db.String(25), nullable=False)
    Street_number=db.Column(db.Integer, nullable=False)
    region= db.Column(db.String(25), nullable=False)
    county= db.Column(db.String(25), nullable=False)
    # relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    
    # relationships
    users = db.relationship('User', backref='addresses', lazy=True)
    

    #Multiple users can have the same address


    def __repr__(self):
        return f"{self.Street_name}, {self.Street_number}>, {self.region},{self.county}>"
    

# Products
class Product(db.Model):
    __tablename__ ="products"
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(25), nullable=False)
    description=db.Column(db.Text, nullable=False)
    category_id=db.Column(db.Integer, db.ForeignKey('product_categories.id'),
        nullable=False)
    image=db.Column(db.String(25), nullable=False)
    price=db.Column(db.Integer, nullable=False)

    users= db.relationship('User', backref='products', lazy=True)
    promotion=db.relationship("Promotion", secondary="product_categories", back_populates="products")

    def __repr__(self):
        return f"{self.name}, {self.description}>, {self.price}"

# Product Category
class ProductCategory(db.Model):
    __tablename__ ="product_categories"
    id= db.Column(db.Integer, primary_key=True)
    category_name=db.Column(db.String(25), nullable=False)

    products=db.relationship('Product', backref='product_categories', lazy=True)
    


    def __repr__(self):
        return f"{self.category_name}"

#promotion- a promotion can have many categories
# a category can have many promotions
class Promotion(db.Model):
    __tablename__ ="promotions"
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(25), nullable=False)
    description=db.Column(db.Text, nullable=False)
    discount_rate=db.Column(db.Integer, nullable=False)
    start_date=db.Column(db.TIMESTAMP, nullable=False)
    end_date=db.Column(db.TIMESTAMP, nullable=False)

    Productcategories= db.relationship('ProductCategory', backref='promotions', lazy=True)


    def __repr__(self):
        return f"{self.name}, {self.description}>, {self.discount_rate}"
    

# shopping cart
class ShoppingCart(db.Model):
    __tablename__ ="shopping_carts"
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    
    shopping_cart_items=db.relationship('ShoppingCartItem', backref='shopping_carts', lazy=True)

    def __repr__(self):
        return f"{self.users_id}"

# Shopping cart not saved unless logged in
class ShoppingCartItem(db.Model):
    __tablename__ ="shopping_cart_items"
    id= db.Column(db.Integer, primary_key=True)
    cart_id= db.Column(db.Integer, db.ForeignKey('shopping_carts.id'),
        nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    product_id= db.Column(db.Integer, db.ForeignKey('products.id'),
        nullable=False)
    quantity=db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.user_id}, {self.quantity}"
  
class ShopOrder(db.Model):
    __tablename__='orders'

    id= db.Column(db.Integer, primary_key=True)
    ordered_date=db.Column(db.TIMESTAMP, nullable=False)
    to_be_delivered_at=db.Column(db.TIMESTAMP, nullable=False)
    order_total = db.Column(db.Integer, nullable=False)
    order_status=db.Column(db.String(25), nullable=False)
    deliver_address =db.Column(db.String(25), nullable=False)
    payment_method =  db.Column(db.String(25), nullable=False)
    
    products=db.relationship("Product", back_populates="orders", lazy=True)



    def __repr__(self):
       return f"<ShopOrder {self.id}, {self.ordered_date}, {self.order_status}, {self.deliver_address}>"



