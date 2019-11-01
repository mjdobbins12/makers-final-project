import pytest

import pawn
import player

test_player_1 = player.Player("test_name_1", "White")
test_pawn = pawn.Pawn("Black")

class TestPlayerProperties:
        def test_player_name(self):
                assert test_player_1.name == "test_name_1"

        def test_player_colour(self):
                assert test_player_1.colour == "White"

        def test_player_captured_pieces_storage(self):
                assert test_player_1.taken_pieces == []

        def test_player_current_score(self):
                assert test_player_1.score == 0

class TestPlayerActions:
        def test_player_captured_pieces(self):
                test_player_1.store_piece(test_pawn)
                assert test_player_1.taken_pieces == [test_pawn]
