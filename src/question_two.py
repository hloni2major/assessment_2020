import enum


class CellState(enum.Enum):
    ALIVE = 1
    DEAD = 2
    REPORDUCE = 3


class Cell:
    def __init__(self, state):
        self.state = state

    def get_next_state(self, neighbours):
        """Gets the next state with number of neighbours"""
        if neighbours < 2:
            self.state = CellState.DEAD
        elif neighbours == 2:
            self.state = CellState.ALIVE


class QuestionTwo:
    """Conway's Game Of Life"""
    pass
