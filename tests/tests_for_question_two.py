import unittest

from src.question_two import QuestionTwo, Cell, CellState


class TestCellWithFewerThanTwoNeighbors(unittest.TestCase):
    """Test: 'Any live cell with fewer than two live neighbours dies, as if by underpopulation.'"""

    def test_cell_dies_when_only_one_neighbor(self):
        """Test: 'Cell with one neighbour'"""
        cell = Cell(state=CellState.ALIVE)
        cell.get_next_state(1)
        self.assertEquals(cell.state, CellState.DEAD)

    def test_cell_with_zero_neighbours_dies(self):
        """Tests 'Cell with no neighbours'"""
        cell = Cell(state=CellState.ALIVE)
        cell.get_next_state(0)
        self.assertEquals(cell.state, CellState.DEAD)


class TestCellWith(unittest.TestCase):
    """Test: 'Any live cell with two or three live neighbours lives on to the next generation.'"""

    def test_cell_lives_on_with_two_neighbours(self):
        """Test: 'Cell lives on with two neighbours.'"""
        cell = Cell(state=CellState)
        cell.get_next_state(2)
        self.assertEquals(cell.state, CellState.ALIVE)


if __name__ == '__main__':
    unittest.main()
