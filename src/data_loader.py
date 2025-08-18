"""
data_loader.py
Module responsible for loading and basic exploration of 311 cases dataset.
Follows single responsibility principle: handles data input and initial exploration.
Updated
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter


class DataLoader:
    """
    Class responsible for loading and basic exploration of 311 cases dataset.
    Follows single responsibility principle: handles data input and initial exploration.
    """
    
    def __init__(self):
        self.data = None
        self.filepath = None
    
    def load_and_explore_data(self, filepath):
        """
        Load the 311 cases dataset and display basic information.
        
        Args:
            filepath (str): Path to the CSV file
            
        Returns:
            pd.DataFrame: Loaded dataset
        """
        self.filepath = filepath
        # TODO: Load the CSV file into self.data
        # TODO: Display basic information about the dataset (shape, columns, info, etc.)
        # TODO: Return the loaded dataset
        pass