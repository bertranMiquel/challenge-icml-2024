import torch

from modules.data.utils.utils import load_manual_mol
from modules.transforms.liftings.graph2cell.ring_lifting import CellRingLifting


class TestCellRingLifting:
    """Test the CellRingLifting class."""

    def setup_method(self):
        # Load the graph
        self.data = load_manual_mol()

        # Initialise the CellCyclesLifting class
        self.lifting = CellRingLifting()

    def test_lift_topology(self):
        # Test the lift_topology method
        lifted_data = self.lifting.forward(self.data.clone())

        expected_incidence_1 = torch.tensor(
                [
                    [1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                    [1., 0., 1., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
                    [0., 0., 1., 0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 1., 0., 0., 1., 0., 0., 1., 1., 0., 0., 0.],
                    [0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0.],
                    [0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 1., 1., 1.],
                    [0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
                    [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]
                ]
            )

        assert (
            expected_incidence_1 == lifted_data.incidence_1.to_dense()
        ).all(), "Something is wrong with incidence_1."

        expected_incidence_2 = torch.tensor(
                [
                    [0., 0.],
                    [0., 0.],
                    [1., 0.],
                    [0., 0.],
                    [1., 1.],
                    [0., 1.],
                    [1., 0.],
                    [0., 0.],
                    [0., 0.],
                    [1., 0.],
                    [0., 0.],
                    [0., 1.],
                    [0., 0.],
                    [0., 0.]
                ]
            )

        assert (
            expected_incidence_2 == lifted_data.incidence_2.to_dense()
        ).all(), "Something is wrong with incidence_2."
