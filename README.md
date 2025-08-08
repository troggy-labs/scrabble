# scrabble

A minimal multiplayer scrabble web app skeleton using Flask with a simple browser front-end.

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run the development server:
   ```bash
   python -m scrabble.server
   ```
   Open `http://localhost:5000/` in your browser to join the game and place tiles.

The server also exposes JSON endpoints:
- `POST /join` to join the game and obtain a player id.
- `GET /board` to fetch the current board and player turn.
- `POST /place` to place a tile (requires `player_id`, `row`, `col`, `letter`).

## Tests

Run the test suite using `unittest`:

```bash
python -m unittest discover -s tests -p 'test*.py' -v
```
