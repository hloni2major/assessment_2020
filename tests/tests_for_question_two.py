import unittest

from src.question_two import QuestionTwo, Cell, CellState


class TestQuestionTwoTests(unittest.TestCase):
    """It tests the rules of conway's game of life."""

    def test_cell_dies_when_only_one_neighbor(self):
        """Tests 'Any live cell with fewer than two live neighbours dies (one neighbour), as if by underpopulation.'"""
        cell = Cell(state=CellState.ALIVE)
        cell.get_next_state(1)
        self.assertEquals(cell.state, CellState.DEAD)

    def test_cell_with_zero_neighbours_dies(self):
        """Tests 'Any live cell with fewer than two live neighbours dies (zero neighbour), as if by underpopulation'"""
        cell = Cell(state=CellState.ALIVE)
        cell.get_next_state(0)
        self.assertEquals(cell.state, CellState.DEAD)


if __name__ == '__main__':
    unittest.main()
