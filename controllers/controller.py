from flask import render_template, request, redirect
from app import app
from models.player import Player
from models.game import Game


@app.route('/')
def base():
    return render_template('welcome.html', title='Rock Paper Scissors')



@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    return render_template('welcome.html', title='Welcome')

@app.route('/play', methods=['POST', 'GET'])
def play():
    return render_template('play.html', title='Play')

@app.route('/result', methods=['POST', 'GET'])
def result():
    player_1_name = request.form.get('player_1_name')
    player_1_choice = request.form.get('player_1_choice')
    player_1 = Player(player_1_name, player_1_choice)
    player_2_name = request.form.get('player_2_name')
    player_2_choice = request.form.get('player_2_choice')
    player_2 = Player(player_2_name, player_2_choice)

    new_game = Game(player_1, player_2)
    result = new_game.winner(player_1, player_2)
    
    return render_template('result.html', player_1_name=player_1_name, player_1_choice=player_1_choice, player_2_name=player_2_name, player_2_choice=player_2_choice, result=result)

    # @app.route('/result', methods=['POST', 'GET'])
    # def result():
    #     return render_template('result.html', title='Results')



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