from flask import render_template, request, redirect
from app import app
from models.player import Player
from models.rock_paper_scissors import RockPaperScissors

@app.route('/')
def index():
    return render_template('index.html', title='Home', )

