import pytest
import game

@pytest.fixture(autouse=True)
def run_before_tests():
    test_game = game.Game('p1', 'p2')
    return test_game

class TestPieceCannotMoveIntoCheck:
    def test_piece_cannot_move_into_check(self, run_before_tests):
        test_game = run_before_tests
        test_game.execute_turn(6,4,5,4)
        test_game.execute_turn(1,5,3,5)
        test_game.execute_turn(7,3,3,7)

        assert test_game.board[0][4].in_check(test_game.board, 0, 4)
        assert test_game.execute_turn(0,4,1,5) == 'invalid move'
        assert test_game.execute_turn(1,0,3,0) == 'invalid move'
        test_game.execute_turn(1,6,2,6)
        assert test_game.board[0][4].in_check(test_game.board, 0, 4) == False

    def test_piece_cannot_expose_king_to_check(self, run_before_tests):
        test_game = run_before_tests
        test_game.execute_turn(6,4,4,4)
        test_game.execute_turn(1,4,3,4)
        test_game.execute_turn(7,3,6,4)
        test_game.execute_turn(1,3,3,3)
        test_game.execute_turn(4,4,3,3)
        test_game.execute_turn(1,2,2,2)
        test_game.execute_turn(6,3,4,3)
        assert test_game.execute_turn(3,4,4,3) == 'invalid move'


