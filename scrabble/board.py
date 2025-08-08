class ScrabbleBoard:
    """Represents a simplified Scrabble board."""

    BOARD_SIZE = 15

    def __init__(self):
        # Initialize a BOARD_SIZE x BOARD_SIZE grid with empty strings
        self.grid = [['' for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]

    def place_tile(self, row, col, letter):
        """Place a tile at the given position."""
        if not (0 <= row < self.BOARD_SIZE and 0 <= col < self.BOARD_SIZE):
            raise ValueError("Position out of bounds")
        if len(letter) != 1 or not letter.isalpha():
            raise ValueError("Tile must be a single alphabetic character")
        self.grid[row][col] = letter.upper()

    def get_tile(self, row, col):
        """Return the tile at the given position."""
        if not (0 <= row < self.BOARD_SIZE and 0 <= col < self.BOARD_SIZE):
            raise ValueError("Position out of bounds")
        return self.grid[row][col]
