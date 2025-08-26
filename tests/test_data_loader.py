import unittest
import pandas as pd
import numpy as np
from unittest.mock import patch, MagicMock
from src.data_loader import DataLoader


class TestDataLoader(unittest.TestCase):
    """Test cases for data_loader module functions."""
