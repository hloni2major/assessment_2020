import unittest

from src.question_two import QuestionTwo, Cell, CellState


class TestCellWithFewerThanTwoNeighbors(unittest.TestCase):
    """Test: 'Any live cell with fewer than two live neighbours dies, as if by underpopulation.'"""

    def test_cell_with_zero_neighbours_dies(self):
        """Tests 'Cell with no neighbours'"""
        cell = Cell(state=CellState.ALIVE)
        state = cell.get_next_state(0)
        self.assertEquals(state,  CellState.DEAD)

    def test_cell_dies_when_only_one_neighbor(self):
        """Test: 'Cell with one neighbour'"""
        cell = Cell(state=CellState.ALIVE)
        state = cell.get_next_state(1)
        self.assertEquals(state,  CellState.DEAD)


class TestCellWithTwoOrThreeNeighbours(unittest.TestCase):
    """Test: 'Any live cell with two or three live neighbours lives on to the next generation.'"""

    def test_cell_lives_on_with_two_neighbours(self):
        """Test: 'Cell lives on with two neighbours.'"""
        cell = Cell(state=CellState)
        state = cell.get_next_state(2)
        self.assertEquals(state,  CellState.ALIVE)

    def test_cell_lives_on_with_three_neighbours(self):
        """Test: 'Cell lives on with three neighbours.'"""
        cell = Cell(state=CellState)
        state = state = cell.get_next_state(3)
        self.assertEquals(state,  CellState.ALIVE)


class TestCellWithMoreThanThreeNeighbours(unittest.TestCase):
    """Test: 'Any live cell with more than three live neighbours dies, as if by overpopulation.'"""

    def test_cell_with_three_neighbours_lives_on(self):
        """Test: 'Cell with three neighbours dies'"""
        cell = Cell(state=CellState.ALIVE)
        state = state = cell.get_next_state(3)
        self.assertEquals(state, CellState.ALIVE)

    def test_cell_with_more_than_three_neighbours_dies(self):
        """Test: 'Cell with more than three neighbours dies'"""
        cell = Cell(state=CellState.ALIVE)
        state = state = cell.get_next_state(4)
        self.assertEquals(state, CellState.DEAD)

    def test_cell_with_five_neighbours_dies(self):
        """Test: 'Cell with more than three neighbours dies'"""
        cell = Cell(state=CellState.ALIVE)
        state = state = cell.get_next_state(5)
        self.assertEquals(state, CellState.DEAD)

    def test_cell_with_six_neighbours_dies(self):
        """Test: 'Cell with more than three neighbours dies'"""
        cell = Cell(state=CellState.ALIVE)
        state = state = cell.get_next_state(6)
        self.assertEquals(state, CellState.DEAD)

    def test_cell_with_seven_neighbours_dies(self):
        """Test: 'Cell with more than three neighbours dies'"""
        cell = Cell(state=CellState.ALIVE)
        state = state = cell.get_next_state(7)
        self.assertEquals(state, CellState.DEAD)


class TestDeadCellWithThreeLiveNeighboursBecomesAlive(unittest.TestCase):
    """Test: 'Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.'"""

    def test_cell_with_three_live_neighbours_reproduces(self):
        """Test: 'Cell with three neighbours becomes alive.'"""
        cell = Cell(state=CellState.DEAD)
        state = cell.get_next_state(3)
        self.assertEquals(state, CellState.ALIVE)


if __name__ == '__main__':
    unittest.main()
