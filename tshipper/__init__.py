"""
Custom class for optimization modeling
of transshipment problems
"""

import pyomo.environ as pe
import pandas as pd


class ShipperModel():
    """
    Pyomo model builder.
    """

    model = pe.ConcreteModel()

    def __init__(
        self,
        supply_data,
        ship_data,
        node_col = 'node',
        supply_col = 'supply',
        capacity_col = 'capacity',
        cost_col = 'cost',
        orig_col = 'node_orig',
        dest_col = 'node_dest'
    ):
        self.supply_data = supply_data
        self.ship_data = ship_data
        self.node_col = node_col
        self.supply_col = supply_col
        self.capacity_col = capacity_col
        self.cost_col = cost_col
        self.orig_col = orig_col
        self.dest_col = dest_col

    def sets(self):
        """
        Define sets for the model.
        """
        n_nodes = self.supply_data[self.node_col].nunique()
        self.model.n_nodes = pe.Set(initialize=range(n_nodes))

    def parameters(self):
        """
        Define model parameters
        """
