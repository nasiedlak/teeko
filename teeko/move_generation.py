import copy

class MoveGeneration:
    def succ(self, state, owner=None):
        piece = self.my_piece if owner == "ai" else self.opp
        drop = self.detectDropPhase(state)
        successors = []

        if drop:
            for i in range(len(state)):
                for j in range(len(state[i])):
                    if state[i][j] == ' ':
                        state_copy = copy.deepcopy(state)
                        state_copy[i][j] = piece
                        successors.append(state_copy)
            return successors

        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == piece:
                    self.add_adjacent(successors, state, i, j, piece)
        return successors

    def add_adjacent(self, successors, state, i, j, piece):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and state[ni][nj] == ' ':
                state_copy = copy.deepcopy(state)
                state_copy[ni][nj] = piece
                state_copy[i][j] = ' '
                successors.append(state_copy)

    def find_move(self, state, next_state, drop_phase=False):
        if drop_phase:
            for i in range(5):
                for j in range(5):
                    if state[i][j] == ' ' and next_state[i][j] != ' ':
                        return [(i, j)]
        else:
            move = [(-1, -1), (-1, -1)]
            for i in range(5):
                for j in range(5):
                    if state[i][j] != ' ' and next_state[i][j] == ' ':
                        move[1] = (i, j)
                    elif state[i][j] == ' ' and next_state[i][j] != ' ':
                        move[0] = (i, j)
            return move
