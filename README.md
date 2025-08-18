> [!CAUTION]
> This repository is for viewing only. Do not work on the assignment using this repository -- the actual course assignments will be provided to you via Pawtograder.

# Homework 3: 311 Service Request Analysis

## Learning Outcomes
By completing this assignment, you will demonstrate proficiency in:
* Using lists, sets, and dictionaries for data manipulation
* Applying the accumulator pattern for data aggregation
* Analyzing real-world datasets using Pandas and NumPy
* Creating data visualizations to reveal patterns
* Critical thinking about algorithmic bias and social equity

## Overview
You will analyze 311 service request data to explore how municipal services are distributed across different neighborhoods and demographics. 311 systems allow residents to report non-emergency issues like potholes, broken streetlights, noise complaints, and other quality-of-life concerns.

### Dataset Options
Choose one of these datasets for your analysis:
* **Oakland/San Francisco**: https://data.sfgov.org/City-Infrastructure/311-Cases/vw6y-z8j6/data_preview
* **Boston**: https://data.boston.gov/dataset/311-service-requests

## Technical Requirements

### Core Functionality
Your analysis must include the following components:

#### 1. Data Loading and Exploration (`data_loader.py`)
* Load the 311 cases dataset using Pandas
* Display basic information about the dataset (shape, columns, data types)
* Identify and handle missing values
* Calculate summary statistics

#### 2. Data Processing and Sorting (`sorting.py`)
* **Add Duration Column**: Calculate how long each request was open (in days)
* **Sort by Duration**: Implement sorting by days open (ascending/descending)
* **Create Urgency Ranking**: Develop a ranking system for case categories based on urgency
  - You must rank at least 10 different categories found in your dataset
  - Use a 1-10 scale where 1 = most urgent, 10 = least urgent
  - Document your reasoning for each ranking in your summary
* **Sort by Urgency**: Sort cases using your custom urgency ranking
* **Filter Data**: Create a filtered dataset containing only the categories you've ranked

#### 3. Geographic Visualization (`visualization.py`)
* Create a scatter plot map showing the geographic distribution of 311 cases
* Use latitude and longitude coordinates to plot cases
* Include appropriate titles and labels
* Save plots as high-quality PNG files

#### 4. Equity Analysis (`analyze_neighborhood_patterns.py`)
* **Above-Average Analysis**: 
  - Calculate the overall average days a case stays open
  - Identify cases that remain open longer than average
  - Count these cases by neighborhood
* **Category Priority Analysis**:
  - Calculate average days open for each category
  - Identify which categories get resolved quickly (priority) vs. slowly (neglected)
* **Neighborhood Volume Analysis**:
  - Count total cases per neighborhood
  - Identify neighborhoods with high vs. low case volumes

### Testing Requirements
* Write comprehensive unit tests for all functions using `unittest`
* Test edge cases, error conditions, and valid inputs
* Use mocking where appropriate for external dependencies
* Achieve good test coverage across all modules

## Ethics and Critical Thinking Component

Write a Stakeholder-Value Matrix for your sorting criteria. Include at least three values and at least five stakeholders. Then, answer the questions in `Summary.md` about algorithmic bias and urban equity.

<!--
### Key Questions to Address in Your Summary:
1. **Urgency Ranking Ethics**: How did you decide which issues are most "urgent"? Consider:
   - Public safety and health impacts
   - Economic consequences for residents
   - Equity and access issues
   - Community impact and quality of life
   - Infrastructure and long-term effects

2. **Bias in Prioritization**: What are the potential consequences of your ranking system? Who might benefit or be harmed?

3. **Neighborhood Patterns**: What patterns do you observe in your data analysis? Do certain neighborhoods consistently have:
   - Longer case resolution times?
   - Different types of service requests?
   - Higher or lower case volumes?

4. **Systemic Issues**: Based on your analysis, what does this suggest about:
   - Resource allocation in city services?
   - Potential discrimination or bias in service delivery?
   - The digital divide and access to 311 systems?
-->

### Documentation:
* `summary.md` - Your analysis results and ethical reflections (see template)
* `README.md` - This file (no changes needed)

### Output Files:
* `311_cases_map.png` - Geographic distribution plot
* Any additional visualizations you create

## Expected Outcome

Through this analysis, you will likely discover that certain neighborhoods consistently receive slower service or have different types of service requests. This reflects real-world patterns of urban inequality and will help you understand how seemingly neutral algorithms can perpetuate or reveal systemic biases.

The goal is not just to implement the technical requirements, but to develop critical thinking skills about the social implications of data analysis and algorithmic decision-making in public services.
