from flask import Flask, jsonify, request
from flask_cors import CORS
from games.models import CardGame

app = Flask(__name__)
CORS(app)

@app.route('/games', methods=['GET'])
def get_games():
    games = CardGame.get_all()
    return jsonify(games)

@app.route('/games', methods=['POST'])
def create_game():
    game_data = request.json
    CardGame.create(game_data)
    return jsonify({"message": "Game created"}), 201

@app.route('/games/<int:game_id>', methods=['POST'])
def update_game(game_id):
    game_data = request.json
    CardGame.update(game_id, game_data)
    return jsonify({"message": "Game updated"})

@app.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    CardGame.delete(game_id)
    return jsonify({"message": "Game deleted"})

if __name__ == '__main__':
    app.run(debug=True)