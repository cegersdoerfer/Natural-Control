from app import db
from flask_sqlalchemy import SQLAlchemy

class Setting(db.Model):
    __tablename__ = 'settings'

    #id = db.Column(db.Integer, primary_key=True)
    brightness = db.Column(db.Integer)
    light_switch = db.Column(db.Boolean)

    def __init__(self, brightness_val=0):
        self.brightness = brightness_val
        self.light_switch = False

    def __repr__(self):
        return '<brightness: {} >'.format(self.brightness)
    
    
