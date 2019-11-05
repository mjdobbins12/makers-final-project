import pytest
import random
import king
from piece import Piece
from king import King
import standard_rules 
import random_pieces 

@pytest.fixture(autouse=True)
def run_before_tests():
        test_ruleset = random_pieces.RandomPieces()
        return test_ruleset

class TestRandomPieces:

        def test_ruleset_inherits_from_standard_rules(self, run_before_tests):
                test_ruleset = random_pieces.RandomPieces()
                assert isinstance(test_ruleset, standard_rules.StandardRules)
                
        def test_ruleset_creates_standard_chess_board(self):
                test_ruleset = random_pieces.RandomPieces()
                assert len(test_ruleset.starting_board) == 8
                assert len(test_ruleset.starting_board[0]) == 8
                
        # def test_ruleset_creates_a_rank_with_king(self):
        #         test_ruleset = random_pieces.RandomPieces()
        #         assert isinstance(test_ruleset.starting_board[0][3], king.King)
