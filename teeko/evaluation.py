import math

class Evaluation:
    def max_value(self, state, d):
        check = self.game_value(state)
        if check in {-1, 1}:
            return check, state

        if d < 3:
            next_state = state
            alpha = -math.inf
            successors = self.succ(state, "ai")
            for s in successors:
                game_value = self.min_value(s, d + 1)[0]
                alpha = max(alpha, game_value)
                if alpha == game_value:
                    next_state = s
            return alpha, next_state

        return self.heuristic_game_value(state)

    def min_value(self, state, d):
        check = self.game_value(state)
        if check in {-1, 1}:
            return check, state

        if d < 3:
            next_state = state
            beta = math.inf
            successors = self.succ(state)
            for s in successors:
                game_value = self.max_value(s, d + 1)[0]
                beta = min(beta, game_value)
                if beta == game_value:
                    next_state = s
            return beta, next_state

        return self.heuristic_game_value(state)

    def heuristic_game_value(self, state):
        current = self.game_value(state)
        if current in (-1, 1):
            return current

        r, b = 0, 0
        for line in self.lines(state):
            r += line.count('r') ** 2
            b += line.count('b') ** 2

        return ((r - b) / (r + b), state) if self.my_piece == 'r' else ((b - r) / (r + b), state)

    def game_value(self, state):
        for row in state:
            for i in range(2):
                if row[i] != ' ' and row[i] == row[i + 1] == row[i + 2] == row[i + 3]:
                    return 1 if row[i] == self.my_piece else -1

        for col in range(5):
            for i in range(2):
                if state[i][col] != ' ' and state[i][col] == state[i + 1][col] == state[i + 2][col] == state[i + 3][col]:
                    return 1 if state[i][col] == self.my_piece else -1

        for i in range(2):
            for j in range(2):
                if state[i][j] != ' ' and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == state[i + 3][j + 3]:
                    return 1 if state[i][j] == self.my_piece else -1

        for i in range(2):
            for j in range(4, 2, -1):
                if state[i][j] != ' ' and state[i][j] == state[i - 1][j - 1] == state[i - 2][j - 2] == state[i - 3][j - 3]:
                    return 1 if state[i][j] == self.my_piece else -1

        for i in range(4):
            for j in range(4):
                if state[i][j] != ' ' and state[i][j] == state[i][j + 1] == state[i + 1][j + 1] == state[i + 1][j]:
                    return 1 if state[i][j] == self.my_piece else -1

        return 0

    def lines(self, state):
        for row in state:
            yield row
        for col in range(5):
            yield [state[row][col] for row in range(5)]
        for d in range(-1, 2):
            yield [state[i][i + d] for i in range(5 - abs(d))]
            yield [state[i][4 - i - d] for i in range(5 - abs(d))]
        for i in range(4):
            for j in range(4):
                yield [state[i][j], state[i][j + 1], state[i + 1][j], state[i + 1][j + 1]]
