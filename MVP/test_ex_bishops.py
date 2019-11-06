import pytest
import piece
import bishop 
import ex_bishops
import standard_rules

@pytest.fixture(autouse=True)
def run_before_tests():
        test_ruleset = ex_bishops.ExBishops()
        return test_ruleset

class TestExBishop:
        def test_ruleset_inherits_from_standard_rules(self, run_before_tests):
                test_ruleset = ex_bishops.ExBishops()
                assert isinstance(test_ruleset, standard_rules.StandardRules)

        def test_generates_random_trigger(self):
                test_ruleset = ex_bishops.ExBishops()
                assert isinstance(test_ruleset.first_trigger, int)
                
        def test_excommunication_of_bishops(self):
                
         