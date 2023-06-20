from django.shortcuts import render
from django.http import HttpResponse
import chess
import chess.svg
from django.contrib.auth.decorators import login_required
# Create your views here.
    
def chessboard(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        print("Client message: " + message)
    # Process the player's message here
    # You can perform validation, update game state, or perform any other logic
    
    # Example response: Return the processed message as a confirmation
        return HttpResponse(f'Message received: {message}')
    else:
        board = chess.Board()
        board.push_san('e4')
        board.push_san('d5')
        board.push_san('exd5')
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

def board(request):
    board = chess.Board()
    squares = chess.SquareSet()
#    img = chess.svg.board(board=board)
    return HttpResponse(chess.svg.board(board=board, squares=squares))
@login_required(login_url='/users/login')
def play_home(request):
    return render(request, 'play.html')
