import unittest
from oxo_logic import newGame, _isWinningMove, userMove, computerMove

class TicTacToeTest(unittest.TestCase):
    """Tests some oxo_logic functions such as
       newGame, _isWinningMove, userMove, computerMove
       (I don't know how to test saveGame, restoreGame, and _generateMove).
    """
    def test_new_game(self):
        game = newGame()
        self.assertEqual(len(game), 9)
        self.assertEqual(game, [" "] * 9)
        
    def test_user_move(self):
        game = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.assertEqual(userMove(game, 0), "")
        self.assertEqual(game, ["X", " ", " ", " ", " ", " ", " ", " ", " "])
        self.assertEqual(userMove(game, 0), ValueError)
        self.assertEqual(userMove(game, 4), "")
        self.assertEqual(game, ["X", " ", " ", " ", "X", " ", " ", " ", " "])
        self.assertEqual(userMove(game, 8), "X")
        
    def test_computer_move(self):
        game = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.assertEqual(computerMove(game), "")
        self.assertIn(game, [["O", " ", " ", " ", " ", " ", " ", " ", " "],
                             [" ", " ", "O", " ", " ", " ", " ", " ", " "],
                             [" ", " ", " ", " ", "O", " ", " ", " ", " "],
                             [" ", " ", " ", " ", " ", " ", "O", " ", " "],
                             [" ", " ", " ", " ", " ", " ", " ", "O", " "],
                             [" ", " ", " ", " ", " ", " ", " ", " ", "O"]])
        self.assertEqual(computerMove(game), "O")
        
    def test_is_winning_move(self):
        game = ["X", "O", "X", "O", "X", " ", " ", " ", " "]
        self.assertFalse(_isWinningMove(game))
        game[5] = "X"
        self.assertTrue(_isWinningMove(game))
        game[5] = "O"
        game[6] = "X"
        self.assertTrue(_isWinningMove(game))
        game[6] = "O"
        game[7] = "X"
        self.assertFalse(_isWinningMove(game))
        
if __name__ == "__main__":
    unittest.main()
