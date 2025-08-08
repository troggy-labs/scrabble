import unittest
import importlib.util

flask_spec = importlib.util.find_spec('flask')

@unittest.skipIf(flask_spec is None, 'Flask not installed')
class TestServerEndpoints(unittest.TestCase):
    def setUp(self):
        from scrabble import server
        self.server = server
        self.client = self.server.app.test_client()
        # reset board and players for each test
        self.server.board = self.server.ScrabbleBoard()
        self.server.players.clear()
        self.server.current_turn = 0

    def test_join_and_place_flow(self):
        # join two players
        res1 = self.client.post('/join')
        p1 = res1.get_json()['player_id']
        res2 = self.client.post('/join')
        p2 = res2.get_json()['player_id']
        self.assertEqual((p1, p2), (1, 2))

        # player 1 places a tile
        r = self.client.post('/place', json={'player_id': p1, 'row':0, 'col':0, 'letter':'a'})
        self.assertEqual(r.status_code, 200)
        # player 2 places a tile
        r = self.client.post('/place', json={'player_id': p2, 'row':0, 'col':1, 'letter':'b'})
        self.assertEqual(r.status_code, 200)
        # player 2 tries again out of turn
        r = self.client.post('/place', json={'player_id': p2, 'row':0, 'col':2, 'letter':'c'})
        self.assertEqual(r.status_code, 400)

if __name__ == '__main__':
    unittest.main()
