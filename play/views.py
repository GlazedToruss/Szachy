from django.shortcuts import render, redirect
from django.http import HttpResponse
import chess
import chess.svg
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from play.models import Game
from django.db import models
# Create your views here.
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str 
def chessboard(request):
    if request.method == 'POST':
        move = request.POST.get('move')
        if 'board' not in request.session:
            board = chess.Board()
            request.session['board'] = board.fen()
        else:
            board = chess.Board(request.session['board'])

        # Perform move validation
        try:
            parsed_move = board.parse_san(move)
            if parsed_move in board.legal_moves:
                board.push(parsed_move)
                valid_move = True
                message = 'Valid move!'
            else:
                valid_move = False
                message = 'Invalid move. Please try again.'
        except ValueError:
            valid_move = False
            message = 'Invalid move. Please try again.'

        # Update the session with the new board state
        request.session['board'] = board.fen()

        # Generate the SVG representation of the updated chessboard
        svg_board = chess.svg.board(board=board)

        # Pass the updated chessboard, validation result, and message to the template
        context = {
            'svg_board': svg_board,
            'valid_move': valid_move,
            'message': message,
        }

        return render(request, 'chessboard.html', context)
    else:
        if 'board' not in request.session:
            board = chess.Board()
            request.session['board'] = board.fen()
        else:
            board = chess.Board(request.session['board'])

        svg_board = chess.svg.board(board=board)
        turn = board.turn
        context = {
            'svg_board': svg_board,
            'turn': turn,
        }
        return render(request, 'chessboard.html', context)



    
def generate_board(request):
    board = chess.Board()
    return HttpResponse(("done generating board: " + board.fen() ))

@login_required(login_url='/users/login')
def play_home(request):
    return render(request, 'play.html')
def board(request):
    board = chess.Board()
    squares = chess.SquareSet()
#    img = chess.svg.board(board=board)
    return HttpResponse(chess.svg.board(board=board, squares=squares))

@login_required(login_url='/users/login')
def play_home(request):
    return render(request, 'play.html')

@login_required(login_url='/users/login')
def history(request):
    return render(request, 'history.html')
@login_required(login_url='/users/login')
def join(request):
    return render(request, )
@login_required
def create_game(request):
    #if request.method == 'POST':
        user = request.user  # Pobranie obiektu aktualnie zalogowanego użytkownika
        id=get_random_string(8)
        game = Game(i_d=id, moves='...', player1=user)
        game.save()
        my_variable='hello'
        context = {'my_variable': my_variable}
        #return render(request, 'waiting_for_player.html', context)
        return redirect(f"/play/new/{id}/", context, id)
       
    #return render(request, 'create_game.html')
@login_required
def waiting_for_player(request, id):
    
    return render(request, 'waiting_for_player.html')
