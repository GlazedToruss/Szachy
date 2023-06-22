from django.shortcuts import render, redirect
from django.http import HttpResponse
import chess
import chess.svg
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from play.models import Game
from django.db import models
import random
import string
from django.shortcuts import get_object_or_404

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str 

def chessboard(request, i_d):
    game = get_object_or_404(Game, i_d=i_d)  # Retrieve the game instance using the provided i_d
    if request.method == 'POST':
        move = request.POST.get('move')
        board = chess.Board(game.moves)
#        if 'board' not in request.session:
#            board = chess.Board()
#            request.session['board'] = board.fen()
#        else:
#            board = chess.Board(request.session['board'])

        # Perform move validation
        try:
            parsed_move = board.parse_san(move)
            if parsed_move in board.legal_moves:
                board.push(parsed_move)
                valid_move = True
                message = 'Valid move!'
                game.moves = board.fen()  # Update the game moves
                game.save()  # Save the game instance
            else:
                valid_move = False
                message = 'Invalid move. Please try again.'
        except ValueError:
            valid_move = False
            message = 'Invalid move. Please try again.'

        # Generate the SVG representation of the updated chessboard
        if valid_move: svg_board = chess.svg.board(board=board, lastmove=parsed_move)
        else: svg_board = chess.svg.board(board=board)
        # Pass the updated chessboard, validation result, and message to the template
        turn = board.turn
        context = {
            'svg_board': svg_board,
            'valid_move': valid_move,
            'message': message,
            'turn': turn,
        }

        return render(request, 'chessboard.html', context)
    else:
#        if 'board' not in request.session:
#            board = chess.Board()
#            request.session['board'] = board.fen()
#        else:
#            board = chess.Board(request.session['board'])
        board = chess.Board(game.moves)

        
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
    #User1 stworzył grę o ID=8817592008
    #User2 używa join by zmienić parametr gry player2 z User1 na User2
    #Następnie flaga Is_waiting zmienia sie na False
    #Następuje przekierowanie do gry


    return render(request)

@login_required
def create_game(request):
    if request.method == 'POST':
        user = request.user  # Pobranie obiektu aktualnie zalogowanego użytkownika
        id=random.randint(1000000000, 9999999999)
        game = Game(i_d=id, moves='', player1=user, player2=user, is_waiting='True')
        game.save()
        my_variable='hello'
        context = {'my_variable': my_variable}
        #return render(request, 'waiting_for_player.html', context)
        return redirect(f"/play/new/{id}/", context, id)
       
    return render(request, 'create_game.html')

@login_required
def waiting_for_player(request, id):
    game = get_object_or_404(Game, i_d=id)
#   Potrzebna logika, sprawdzająca czy obiekt gry o 'i_d = game_id', ma flagę 'game_is_waiting' ustawioną na True czy na False
    if Game.is_waiting:
        return render(request, 'waiting_for_player.html', {'i_d': id})
    else:
        return redirect('chessboard', i_d=id)

#@login_required(login_url='/users/login')
#def play_game(request, game_id):
#    game = Game.objects.get(is_waiting=game_id)
#    return redirect('chessboard', request, game=game)

