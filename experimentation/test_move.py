import move

board = move.Board()

class TestMove:
        def test_move(self):
                board.move(2,4,4,3)
                assert board.show_board() == [
								['B','B','B','B','B','B','B','B'],
                ['B','B','B','B','B','B','B','B'],
                ['B','B','B','B','B','B','B','B'],
                ['B','B','B','B','B','B','B','B'],
                ['B','B','B','*','B','B','B','B'],
                ['B','B','B','B','B','B','B','B'],
                ['B','B','B','B','B','B','B','B'],
                ['B','B','B','B','B','B','B','B']
              ]
        