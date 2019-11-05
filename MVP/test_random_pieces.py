# it creates a board with 64 elements
# it creates a rank with a king
# it creates a rank without a king

from piece import Piece
from king import King
import standard_rules 
import pytest
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




