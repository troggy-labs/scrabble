import unittest
from scrabble.board import ScrabbleBoard


class TestScrabbleBoard(unittest.TestCase):
    def test_board_initialization(self):
        board = ScrabbleBoard()
        self.assertEqual(len(board.grid), board.BOARD_SIZE)
        self.assertTrue(all(len(row) == board.BOARD_SIZE for row in board.grid))

    def test_place_and_get_tile(self):
        board = ScrabbleBoard()
        board.place_tile(7, 7, 'a')
        self.assertEqual(board.get_tile(7, 7), 'A')


if __name__ == '__main__':
    unittest.main()
