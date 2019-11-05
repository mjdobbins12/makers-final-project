# after a certain time the bishops are deleted 

# after a certain time the bishops of one player are deleted

# after a certain time the bishops' behaviour for one player changed 

# then the other player 

# same for knights

# ROOKS
# same for rooks - sells them to the other side 

import random
import piece 
import bishop
from standard_rules import StandardRules

class ExBishops(StandardRules):
        def __init__(self):
                super().__init__()
                self.first_trigger = random.randint(2, 6)
        
        def check_logs(self, board, piece, log):
                if len(log) >= self.first_trigger and piece.colour == "White":
                        self.excommunicate_bishops(board, "Black")
                else: 
                        self.excommunicate_bishops(board, "White")
                          
        def excommunicate_bishops(self, board, colour):
                for i in range(8):
                        print(i)
                        for j in range(8):
                                if isinstance(board[i][j], bishop.Bishop):
                                        if board[i][j].colour == colour:
                                                board[i][j] = '-'
                                                print(f"Oh no! {colour} bishops were excommunicated!")
                        
