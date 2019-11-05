import pytest
import game
import king
from game import Game
from piece import Piece
from standard_rules import StandardRules

@pytest.fixture(autouse=True)
def run_before_tests():
        test_game = game.Game('p1', 'p2', ruleset = StandardRules())
        return test_game

class TestAvailableMoves:
        def test_pawn_has_only_2_available_start_moves(self, run_before_tests):
                test_game = run_before_tests
                assert test_game.board[6][0].available_moves(test_game.board, 6, 0) == [[4,0],[5,0]]

        def test_knight_has_only_2_available_start_moves(self, run_before_tests):
                test_game = run_before_tests
                assert test_game.board[0][1].available_moves(test_game.board, 0, 1) == [[2,0],[2,2]]

        def test_Queen_has_only_2_available_moves_forward(self, run_before_tests):
                test_game = run_before_tests
                test_game.execute_turn(6, 3, 4, 3)
                test_game.execute_turn(1, 5, 3, 5)
                assert test_game.board[7][3].available_moves(test_game.board, 7, 3) == [[5,3],[6,3]]

        def test_Queen_has_only_4_available_moves_diagonally(self, run_before_tests):
                test_game = run_before_tests
                test_game.execute_turn(6, 4, 4, 4)
                test_game.execute_turn(1, 5, 3, 5)
                assert test_game.board[7][3].available_moves(test_game.board, 7, 3) == [[3,7],[4,6],[5,5],[6,4]]

