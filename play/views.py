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
        svg_board = chess.svg.board(board=board)
        turn = board.turn
        context = {
            'svg_board': svg_board,
            'turn': turn,
        }
        return render(request, 'chessboard.html', context)
    
def generate_board(request):
    board = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
    return HttpResponse("done generating board")

@login_required(login_url='/users/login')
def play_home(request):
    return render(request, 'play.html')