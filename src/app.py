from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from slider import Slider
#from forms import *
import os
import traceback
import datetime
from pytz import timezone

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class Setting(db.Model):
    __tablename__ = 'settings'

    id = db.Column(db.Integer, primary_key=True)
    brightness = db.Column(db.Integer)
    light_switch = db.Column(db.Boolean)

    def __init__(self, brightness_val=0, light_switch=False):
        self.id = 1
        self.brightness = brightness_val
        self.light_switch = light_switch

    def __repr__(self):
        return '<val: {}, switch: {}>'.format(self.brightness, self.light_switch)
    
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    slider_val = 0
    switch_val = False
    # print all columns in settings table
    if db.session.query(Setting.id).all() == []:
        db.session.add(Setting(slider_val, switch_val))
    else:
        res = Setting.query.first()
        slider_val = res.brightness
        switch_val = res.light_switch

    return render_template('home.html', slider=slider_val, switch_val=switch_val)

@app.route('/brightness', methods=['GET', 'POST'])
def slider():
    # get slider value from db
    data = request.get_json()
    brightness_val = data['brightness']
    if request.method == 'GET':
        try:
            res = Setting.query.first()
            slider_val = res.brightness
            return jsonify({'success': True, 'slider': slider_val})
        except:
            return jsonify({'success': False, 'trace': traceback.format_exc()})
    else:
        try:
            db.session.query(Setting).filter_by(id=1).update(dict(brightness=brightness_val))
            db.session.commit()
            return jsonify({'success': True})
        except:
            return jsonify({'success': False, 'trace': traceback.format_exc()})

@app.route('/switch', methods=['GET', 'POST'])
def toggle_light_switch():
    data = request.get_json()
    switch_val = data['lightSwitch']
    # update light switch value in db at id 1
    if request.method == 'GET':
        try:
            res = Setting.query.first()
            switch_val = res.light_switch
            return jsonify({'success': True, 'switch': switch_val})
        except:
            return jsonify({'success': False, 'trace': traceback.format_exc()})
    else:
        try:
            db.session.query(Setting).filter_by(id=1).update(dict(light_switch=switch_val))
            db.session.commit()
            return jsonify({'success': True})
        except:
            return jsonify({'success': False, 'trace': traceback.format_exc()})
        
@app.route('/time', methods=['GET'])
def get_time():
    zone = timezone('EST')
    time = datetime.datetime.now(zone)
    hours = time.hour
    minutes = time.minute
    seconds = time.second
    return jsonify({'success': True, 'hour': hours, 'minute': minutes, 'second': seconds})
    

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
    app.run(port=5000, debug=True)