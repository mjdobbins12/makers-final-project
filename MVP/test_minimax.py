import game
import minimax
import pytest



@pytest.fixture(autouse=True)
def run_before_tests():
        new_game = game.Game('p1', 'p2') 
        test_minimax = minimax.Minimax(new_game)
        return test_minimax

class TestInputOutput:
        def test_accepts_two_args(self, run_before_tests):
                test_minimax = run_before_tests
                new_minimax = minimax.Minimax(test_minimax.game)

        def test_outputs_a_move(self, run_before_tests):
                test_minimax = run_before_tests
                test_minimax.game.execute_turn(6, 4, 4, 4)
                assert isinstance(test_minimax.execute_turn(), list)

class TestValueOfMoves:
        def test_value_of_available_moves_for_next_move(self, run_before_tests):
                test_minimax = run_before_tests
                assert isinstance(test_minimax.all_possible_moves(test_minimax.game.board.board), list)


class TestAllAvailableMoves:
        def test_returns_available_moves_white(self, run_before_tests):
                test_minimax = run_before_tests
                assert test_minimax.available_moves(test_minimax.game.board.board) == [
                        [[6, 0], [[4, 0], [5, 0]]], 
                        [[6, 1], [[4, 1], [5, 1]]], 
                        [[6, 2], [[4, 2], [5, 2]]], 
                        [[6, 3], [[4, 3], [5, 3]]], 
                        [[6, 4], [[4, 4], [5, 4]]], 
                        [[6, 5], [[4, 5], [5, 5]]], 
                        [[6, 6], [[4, 6], [5, 6]]], 
                        [[6, 7], [[4, 7], [5, 7]]], 
                        [[7, 0], []], 
                        [[7, 1], [[5, 0], [5, 2]]], 
                        [[7, 2], []],
                        [[7, 3], []], 
                        [[7, 4], [[7, 2], [7, 6]]], 
                        [[7, 5], []], 
                        [[7, 6], [[5, 5], [5, 7]]], 
                        [[7, 7], []]
                        ]
                        

        def test_returns_available_moves_black(self, run_before_tests):
                test_minimax = run_before_tests
                test_minimax.game.execute_turn(6,4,4,4)
                assert test_minimax.available_moves(test_minimax.game.board.board) == [
                        [[0, 0], []],
                        [[0, 1], [[2, 0], [2, 2]]],
                        [[0, 2], []], 
                        [[0, 3], []], 
                        [[0, 4], [[0, 2], [0, 6]]], 
                        [[0, 5], []], 
                        [[0, 6], [[2, 5], [2, 7]]], 
                        [[0, 7], []], 
                        [[1, 0], [[2, 0], [3, 0]]], 
                        [[1, 1], [[2, 1], [3, 1]]], 
                        [[1, 2], [[2, 2], [3, 2]]], 
                        [[1, 3], [[2, 3], [3, 3]]], 
                        [[1, 4], [[2, 4], [3, 4]]], 
                        [[1, 5], [[2, 5], [3, 5]]], 
                        [[1, 6], [[2, 6], [3, 6]]], 
                        [[1, 7], [[2, 7], [3, 7]]]
                        ]

class TestMiniMax:
        def test_return_value_from_minimax(self, run_before_tests):
                test_minimax = run_before_tests
                assert len(test_minimax.minimax(2)) == 143
                

class TestMiniMaxEvaluation:
        def test_move_chosen(self, run_before_tests):
                test_minimax = run_before_tests



