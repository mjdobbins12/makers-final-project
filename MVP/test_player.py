import pytest
import pawn
import player

test_pawn = pawn.Pawn("Black")

class TestPlayerProperties:
        def test_player_name(self):
                test_player_1 = player.Player("test_name_1", "White")
                assert test_player_1.name == "test_name_1"

        def test_player_colour(self):
                test_player_1 = player.Player("test_name_1", "White")
                assert test_player_1.colour == "White"

        def test_player_captured_pieces_storage(self):
                test_player_1 = player.Player("test_name_1", "White")
                assert test_player_1.taken_pieces == []

        def test_player_current_score(self):
                test_player_1 = player.Player("test_name_1", "White")
                assert test_player_1.current_score == 0

class TestPlayerActions:
        def test_player_captured_pieces(self):
                test_player_1 = player.Player("test_name_1", "White")
                test_player_1.store_piece(test_pawn)
                assert test_player_1.taken_pieces == [test_pawn]
                
        def test_update_score(self):
                test_player_1 = player.Player("test_name_1", "White")
                test_player_1.store_piece(test_pawn)
                assert test_player_1.current_score == 1
                
                
                
