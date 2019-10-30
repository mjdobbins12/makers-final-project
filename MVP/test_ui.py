import pytest
import ui


class TestUI:

        def test_get_names(self):
            input = ['Batman', 'Superman']
            ui.input = lambda x: input.pop(0)
            test_ui = ui.UI()
            output = test_ui.get_names()
            assert output[0] == 'Batman'
            assert output[1] == 'Superman'

        def teardown_method(self, method):
        # This method is being called after each test case, and it will revert input back to original function
            ui.input = input
