from datetime import datetime
import enum

from api import db

class ClientType(enum.Enum):
    CLIENT_A = "Client A"
    CLIENT_B = "Client B"
    CLIENT_C = "Client C"

class ProductAreaType(enum.Enum):
    POLICIES = "Policies"
    BILLING = "Billing"
    CLAIMS = "Claims"
    REPORTS = "Reports"


class Feature(db.Model):
    """
    Create a Feature table
    """

    __tablename__ = 'features'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    client = db.Column(db.Enum(ClientType))
    client_priority = db.Column(db.Integer)
    target_date = db.Column(db.DateTime, default=datetime.utcnow)
    product_area = db.Column(db.Enum(ProductAreaType))


    def __repr__(self):
        return '<Feature: {}>'.format(self.name)