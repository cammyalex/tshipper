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

    def __init__(self) -> None:
        pass
