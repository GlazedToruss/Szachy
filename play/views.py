from django.shortcuts import render
from django.http import HttpResponse
import chess
import chess.svg
from django.contrib.auth.decorators import login_required
# Create your views here.
    
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

def board(request):
    board = chess.Board()
    squares = chess.SquareSet()
#    img = chess.svg.board(board=board)
    return HttpResponse(chess.svg.board(board=board, squares=squares))
@login_required(login_url='/users/login')
def play_home(request):
    return render(request, 'play.html')
