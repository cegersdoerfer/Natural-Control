from flask import Flask, render_template, request, redirect, url_for
import logging
from logging import Formatter, FileHandler
from slider import Slider
import serial
#from forms import *
import os
from arduino_setup import setup

app = Flask(__name__)
app.config.from_object('config')

#pwm = setup()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        slider_val = request.form['brightness-slider']
    else:
        slider_val = 0
    return render_template('home.html', slider=slider_val)

@app.route('/slider', methods=['POST'])
def slider():
    slider_val = request
    return slider_val
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