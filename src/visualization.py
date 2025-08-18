"""
visualization.py
Module responsible for creating geographic visualizations of 311 cases.
Focuses on mapping and visual analysis of spatial patterns.
Updated
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter


class Visualization:
    """
    Class responsible for creating geographic visualizations of 311 cases.
    Focuses on mapping and visual analysis of spatial patterns.
    """
    
    def __init__(self, data=None):
        self.data = data
        self.setup_plotting_style()
    
    def setup_plotting_style(self):
        """Set up consistent plotting style for all visualizations."""
        # TODO: Set up plotting style (seaborn style, figure size defaults, etc.)
        pass
    
    def set_data(self, data):
        """Set the dataset for visualization."""
        self.data = data
    
    def plot_cases_on_map(self, title="311 Cases Geographic Distribution", save_path=None):
        """
        Create a plot (on a map) of 311 cases using latitude and longitude coordinates.
        
        Args:
            title (str): Title for the plot
            save_path (str, optional): Path to save the plot as PNG
            
        Returns:
            tuple: (figure, axes) matplotlib objects
            
        Raises:
            KeyError: If latitude/longitude columns are missing
            ValueError: If no valid coordinates are found
        """
        if self.data is None:
            raise ValueError("No data set. Please call set_data() first.")
        
        # TODO: Ensure that the required columns are present in the data
        # TODO: Remove rows with missing coordinates
        # TODO: Create the plot
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to: {save_path}")
        
        plt.show()
        
        pass