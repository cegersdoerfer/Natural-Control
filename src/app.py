from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from slider import Slider
import serial
#from forms import *
import os
from arduino_setup import setup

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

class Setting(db.Model):
    __tablename__ = 'settings'

    id = db.Column(db.Integer, primary_key=True)
    brightness = db.Column(db.Integer)

    def __init__(self, brightness_val=0):
        self.id = 1
        self.brightness = brightness_val

    def __repr__(self):
        return '<val {}>'.format(self.brightness)
with app.app_context():
    db.create_all()


#pwm = setup()

@app.route('/', methods=['GET', 'POST'])
def home():
    slider_val = 0
    # print all columns in settings table
    if request.method == 'POST':
        slider_val = request.form['brightness-slider']
        if db.session.query(Setting.id).all() == []:
            db.session.add(Setting(int(slider_val)))
        else:
            # update brightness value in db at id 1
            db.session.query(Setting).filter_by(id=1).update(dict(brightness=slider_val))
    else:
        if db.session.query(Setting.id).all() == []:
            db.session.add(Setting(slider_val))
        else:
            slider_val = Setting.query.first().brightness
    db.session.commit()
    return render_template('home.html', slider=slider_val)

@app.route('/slider', methods=['POST'])
def slider():
    # get slider value from db
    slider_val = Setting.query.first().brightness
    return str(slider_val)
    #return pwm.analog_write(11, slider_val)

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

if __name__ == '__main__':
    app.run()