from app import db
from flask_sqlalchemy import SQLAlchemy

class Setting(db.Model):
    __tablename__ = 'settings'

    #id = db.Column(db.Integer, primary_key=True)
    brightness = db.Column(db.Integer)

    def __init__(self, brightness_val=0):
        self.brightness = brightness_val

    def __repr__(self):
        return '<val {}>'.format(self.brightness)
    
    
