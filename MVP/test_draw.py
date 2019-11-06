import pytest

from game import Game

@pytest.fixture(autouse=True)
def run_before_tests():
        test_game = Game("p1", "p2")
        return test_game

class TestDraw:
    def test_game_does_not_begin_in_stalemate(self, run_before_tests):
        test_game = run_before_tests
        assert test_game.is_draw() == False

    def test_stalemate_scenario(self, run_before_tests):
        test_game = run_before_tests
        test_game.execute_turn(6,4,5,4)
        test_game.execute_turn(1,0,3,0)
        test_game.execute_turn(7,3,3,7)
        test_game.execute_turn(0,0,2,0)
        test_game.execute_turn(3,7,3,0)
        test_game.execute_turn(1,7,3,7)
        test_game.execute_turn(6,7,4,7)
        test_game.execute_turn(2,0,2,7)
        test_game.execute_turn(3,0,1,2)
        test_game.execute_turn(1,5,2,5)
        test_game.execute_turn(1,2,1,3)
        test_game.execute_turn(0,4,1,5)
        test_game.execute_turn(1,3,1,1)
        test_game.execute_turn(0,3,5,3)
        test_game.execute_turn(1,1,0,1)
        test_game.execute_turn(5,3,1,7)
        test_game.execute_turn(0,1,0,2)
        test_game.execute_turn(1,5,2,6)
        test_game.execute_turn(0,2,2,4)
        assert test_game.is_draw()
