import copy

class BoardOperations:
    board = [[' ' for _ in range(5)] for _ in range(5)]

    def detectDropPhase(self, state):
        count = sum(cell != ' ' for row in state for cell in row)
        return count < 8

    def place_piece(self, move, piece):
        if len(move) > 1:
            self.board[move[1][0]][move[1][1]] = ' '
        self.board[move[0][0]][move[0][1]] = piece

    def validate_opponent_move(self, move):
        if len(move) > 1:
            src_row, src_col = move[1]
            if self.board[src_row][src_col] != self.opp:
                self.print_board()
                raise Exception("You don't have a piece there!")
            if abs(src_row - move[0][0]) > 1 or abs(src_col - move[0][1]) > 1:
                self.print_board()
                raise Exception('Illegal move: Can only move to an adjacent space')
        if self.board[move[0][0]][move[0][1]] != ' ':
            raise Exception("Illegal move detected")
