import pytest

import player

test_player_1 = player.Player("test_name_1", "White")

class TestPlayerProperties:
        def test_player_name(self):
                assert test_player_1.name == "test_name_1"

        # def test_player_colour(self):
        # 	assert test_rook_b.symbol == '♜'
        # 	assert test_rook_w.symbol == '♖'
