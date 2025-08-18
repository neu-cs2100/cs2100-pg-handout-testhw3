"""
sorting.py
Module responsible for sorting 311 cases and managing urgency rankings.
Combines sorting and urgency functions as they work together conceptually.
Updated
"""

import pandas as pd
import numpy as np

class Sorting:
    """
    Class responsible for sorting 311 cases and managing urgency rankings.
    Combines sorting and urgency functions as they work together conceptually.
    """
    
    def __init__(self, data=None):
        self.data = data
        self.urgency_ranking = {}
        self.filtered_data = None
    
    def set_data(self, data):
        """Set the dataset for this sorter."""
        self.data = data
    
    def sort_by_days_open(self, ascending=False):
        """
        Sort the 311 cases by how long they were open.
        
        Args:
            ascending (bool): If True, sort from shortest to longest duration
            
        Returns:
            pd.DataFrame: Sorted dataset
            
        Raises:
            KeyError: If 'days_open' column doesn't exist
            ValueError: If days_open contains non-numeric values
        """
        if self.data is None:
            raise ValueError("No data set. Please call set_data() first.")
        
        # TODO: Sort the data by days_open
        # TODO: Handle errors for missing column or non-numeric values
        pass
    
    def create_urgency_ranking(self):
        """
        Create an urgency ranking system for 311 case categories.
        
        ETHICS QUESTION FOR STUDENTS: (Will add these in the summary file)
        How do you decide which issues are most "urgent"? 
        Consider factors like:
        - Public safety and health impacts
        - Economic consequences
        - Equity and access issues
        - Community impact and quality of life
        - Infrastructure and long-term effects
        
        Returns:
            dict: Dictionary mapping categories to urgency scores (1 = most urgent, higher = less urgent)
        """
        if self.data is None:
            raise ValueError("No data set. Please call set_data() first.")
            
        if 'category' not in self.data.columns:
            print("Warning: 'category' column not found in dataset")
            return {}
        
        # Get all unique categories
        categories = self.data['category'].unique()
        print("Available categories in your dataset:")
        print("-" * 40)
        for i, cat in enumerate(sorted(categories), 1):
            print(f"{i:2d}. {cat}")
        
        print(f"\nTotal categories: {len(categories)}")
        
        # TODO: Students should create their urgency ranking here
        # This is a placeholder - students should modify this based on their reasoning
        # Lower numbers = more urgent (1 is most urgent)
        self.urgency_ranking = {
            # EXAMPLE (students should replace with their own reasoning):
            # 'Traffic Signal Repair': 1,           # Immediate safety risk
            # 'Street Defects': 2,                 # Safety and accessibility 
            # 'Blocked Bike Lane': 3,              # Safety and transportation
            # 'Street and Sidewalk Cleaning': 4,   # Quality of life
            #  And so on
            
            # TODO: Add rankings for at least 10 categories found in your dataset
            # Use the list above to assign urgency scores (1-10 scale recommended)
        }
        
        return self.urgency_ranking
    
    def filter_data(self):
        """
        Filter the dataset to include only the categories that have been ranked.
        
        Returns:
            pd.DataFrame: Filtered dataset
        """
        if self.data is None:
            raise ValueError("No data set. Please call set_data() first.")
            
        if not self.urgency_ranking:
            raise ValueError("No urgency ranking created. Please call create_urgency_ranking() first.")
        
        # TODO: Filter the dataset to include only the categories you have ranked
        # Store result in self.filtered_data
        pass