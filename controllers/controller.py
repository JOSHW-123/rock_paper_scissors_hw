from flask import render_template, request, redirect
from app import app
from models.player import Player
from models.game import Game


@app.route('/')
def base():
    return render_template('welcome.html', title='Rock Paper Scissors')

@app.route('/result', methods=['POST', 'GET'])
def result():
    return render_template('result.html', title='Results')

@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    return render_template('welcome.html')

@app.route('/play', methods=['POST'])
def play():
    return render_template('welcome.html')


# @app.route('/events', methods=['POST'])
# def add_event():
#     event_name = request.form['name_of_event']
#     event_description = request.form['description']
#     event_date = request.form['date']
#     event_location = request.form['location']
#     event_number_of_guests = request.form['number_of_guests']
#     # event_recurring = request.form['recurring']
#     new_event = Event(event_date, event_name, event_number_of_guests, event_location, event_description)
#     add_new_event(new_event)
#     return redirect('/events')