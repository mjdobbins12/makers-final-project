import random
import piece 
import bishop
import rook 
import un_rook
from standard_rules import StandardRules

class ExBishops(StandardRules):
        def __init__(self):
                super().__init__()
                self.first_trigger = random.randint(1, 4)
                self.second_trigger = random.randint(5, 8)
                self.third_trigger = self.second_trigger + 10
        
        def check_logs(self, board, piece, log):
                self.turn_number = len(log) # use to take a snapshot for timing rook transactions
                
                
                # timing for excommunication of bishops 
                
                if self.turn_number >= self.first_trigger: 
                        if piece.colour == "White":
                                self.excommunicate_bishops(board, "Black")
                        elif piece.colour == "Black":
                                self.excommunicate_bishops(board, "White")
                        self.first_trigger = 100 # not needed if make condition just = instead of >=
                        
        
                # timing for starting sale of rooks 
                
                if self.turn_number >= self.second_trigger:
                        if piece.colour == "White":
                                self.start_sale_of_rooks(board, "Black", "White")
                        elif piece.colour == "Black": 
                                self.start_sale_of_rooks(board, "White", "Black")
                        self.second_trigger = 100
                                                  
        def excommunicate_bishops(self, board, colour):
                for i in range(8):
                        print(i)
                        for j in range(8):
                                if isinstance(board[i][j], bishop.Bishop):
                                        if board[i][j].colour == colour:
                                                board[i][j] = '-'
                                                print(f"Oh no! {colour} bishops were excommunicated!")
        
        def start_sale_of_rooks(self, board, colour_1, colour_2):
                for i in range(8):
                        print(i)
                        for j in range(8):
                                if isinstance(board[i][j], rook.Rook):
                                        if board[i][j].colour == colour_1:
                                                board[i][j] = un_rook.UnRook(colour_2)
                                                print(f"Oh no! {colour_1} rooks were sold off! They can't move for 5 turns, while the transaction completes.")
                                                