import pytest
import piece
import bishop 
import ex_bishops

@pytest.fixture(autouse=True)
def run_before_tests():
        test_ruleset = ex_bishops.ExBishops()
        return test_ruleset

class TestExBishop:
        def test_generates_random_trigger(self):
                test_ruleset = ex_bishops.ExBishops()
                assert isinstance(test_ruleset.first_trigger, int)
                
         