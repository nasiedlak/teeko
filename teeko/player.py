import random
from .board import BoardOperations
from .move_generation import MoveGeneration
from .evaluation import Evaluation

class TeekoPlayer(BoardOperations, MoveGeneration, Evaluation):
    """ An object representation for an AI game player for the game Teeko.
    """
    pieces = ['b', 'r']

    def __init__(self):
        """ Initializes a TeekoPlayer object by randomly selecting red or black as its piece color.
        """
        self.my_piece = random.choice(self.pieces)
        self.opp = self.pieces[0] if self.my_piece == self.pieces[1] else self.pieces[1]
        super().__init__()

    def make_move(self, state):
        """ Selects a (row, col) space for the next move.
        """
        if not self.detectDropPhase(state):
            _, next_state = self.max_value(state, 0)
            return self.find_move(state, next_state)

        _, next_state = self.max_value(state, 0)
        return self.find_move(state, next_state, drop_phase=True)
    
    def opponent_move(self, move):
        """ Validates the opponent's next move against the internal board representation.
        """
        self.validate_opponent_move(move)
        self.place_piece(move, self.opp)

    def print_board(self):
        """ Formatted printing for the board """
        for row in range(len(self.board)):
            line = str(row) + ": "
            for cell in self.board[row]:
                line += cell + " "
            print(line)
        print("   A B C D E")
