from datetime import datetime
import enum
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login
from app import db

class User(UserMixin, db.Model):
    """
    Create an User table
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

# Set up user_loader
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class ClientType(enum.Enum):
    CLIENT_A = "Client A"
    CLIENT_B = "Client B"
    CLIENT_C = "Client C"

    @classmethod
    def choices(cls):
        return [(choice.name, choice.name) for choice in cls]

    @classmethod
    def stringify(cls, val):
        for choice in cls:
            if choice.name==val.name:
                return choice.value

class ProductAreaType(enum.Enum):
    POLICIES = "Policies"
    BILLING = "Billing"
    CLAIMS = "Claims"
    REPORTS = "Reports"

    @classmethod
    def choices(cls):
        return [(choice.name, choice.name) for choice in cls]

    @classmethod
    def stringify(cls, val):
        for choice in cls:
            if choice.name==val.name:
                return choice.value


class Client(db.Model):
    """
    Create a Client table
    """

    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.Enum(ClientType))
    client_priority = db.Column(db.Integer)
    features = db.relationship('Feature', backref='client', lazy=True)

    def __repr__(self):
        return '<Client: {}>'.format(self.client)

class Feature(db.Model):
    """
    Create a Feature table
    """

    __tablename__ = 'features'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'),
        nullable=False)    
    target_date = db.Column(db.DateTime)
    product_area = db.Column(db.Enum(ProductAreaType))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.now)


    def __repr__(self):
        return '<Feature: {}>'.format(self.title)