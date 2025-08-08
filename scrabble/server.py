from flask import Flask, jsonify, request, render_template
from .board import ScrabbleBoard

app = Flask(__name__)

board = ScrabbleBoard()
players = []
current_turn = 0

@app.route('/')
def index():
    """Serve the main game page."""
    return render_template('index.html')

@app.route('/board')
def get_board():
    """Return the current board state and current player."""
    current_player = players[current_turn] if players else None
    return jsonify({'board': board.grid, 'current_player': current_player})

@app.route('/join', methods=['POST'])
def join_game():
    """Add a new player to the game and return their ID."""
    player_id = len(players) + 1
    players.append(player_id)
    return jsonify({'player_id': player_id})

@app.route('/place', methods=['POST'])
def place_tile():
    """Place a tile on the board if it's the player's turn."""
    global current_turn
    data = request.get_json()
    player_id = data.get('player_id')
    row = data.get('row')
    col = data.get('col')
    letter = data.get('letter')

    if not players or players[current_turn] != player_id:
        return jsonify({'error': 'Not your turn'}), 400

    try:
        board.place_tile(row, col, letter)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    current_turn = (current_turn + 1) % len(players)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
