import random
import piece 
import bishop
import rook 
import un_rook
import knight
import sp_knight
from standard_rules import StandardRules

class ExBishops(StandardRules):
        def __init__(self):
                super().__init__()
                
                # self.first_trigger = random.randint(1, 4)
                # self.second_trigger = random.randint(5, 8)
                # self.third_trigger = random.randint(9, 11)
                
                self.first_trigger = 3
                self.second_trigger = 5
                self.third_trigger = 7
                self.fourth_trigger = 9
                self.fifth_trigger = 11
                
        def check_special_events(self, board, piece, log):
                self.turn_number = len(log) 
                  
                if self.turn_number >= self.first_trigger: 
                        if piece.colour == "White":
                                self.excommunicate_bishops(board, "Black")
                        elif piece.colour == "Black":
                                self.excommunicate_bishops(board, "White")
                        self.first_trigger = 100 
                        
                if self.turn_number >= self.second_trigger:
                        if piece.colour == "White":
                                self.start_sale_of_rooks(board, "Black", "White")
                        elif piece.colour == "Black": 
                                self.start_sale_of_rooks(board, "White", "Black")
                        self.second_trigger = 100
                          
                if self.turn_number >= self.third_trigger:   
                        self.complete_sale_of_rooks(board)
                        self.third_trigger = 100
                        
                if self.turn_number >= self.fourth_trigger:   
                        self.honour_knights(board)
                        self.fourth_trigger = 100
                
                if self.turn_number >= self.fifth_trigger:
                        self.return_knights_to_normal(board)
                        self.fifth_trigger = 100
                
                   
        def excommunicate_bishops(self, board, colour):
                for i in range(8):
                        for j in range(8):
                                if isinstance(board[i][j], bishop.Bishop):
                                        if board[i][j].colour == colour:
                                                board[i][j] = '-'
                                                print(f"Oh no! {colour} bishops were excommunicated!")
        
        def start_sale_of_rooks(self, board, colour_1, colour_2):
                for i in range(8):
                        for j in range(8):
                                if isinstance(board[i][j], rook.Rook):
                                        if board[i][j].colour == colour_1:
                                                board[i][j] = un_rook.UnRook(colour_2)
                                                print(f"Oh no! {colour_1} rooks were sold off! They can't move for 5 turns, while the transaction completes.")
                                                
        def complete_sale_of_rooks(self, board):
                for i in range(8):
                        for j in range(8):
                                if isinstance(board[i][j], un_rook.Rook):
                                        colour = board[i][j].colour
                                        board[i][j] = rook.Rook(colour)
                                        print("Sale complete! All Rooks can move again.")
                                        
        def honour_knights(self, board):
                for i in range(8):
                        for j in range(8):
                                if isinstance(board[i][j], knight.Knight):
                                        colour = board[i][j].colour
                                        board[i][j] = sp_knight.SpKnight(colour)
                                        print("Knights receive the hightest honour! They can move in any direction for 1 turn.")
                                        
        def return_knights_to_normal(self, board):
                for i in range(8):
                        for j in range(8):
                                if isinstance(board[i][j], sp_knight.SpKnight):
                                        colour = board[i][j].colour
                                        board[i][j] = knight.Knight(colour)
                                        print("Ah, the fun has worn off - knights back to normal")
                                        
                                        
        
                                                