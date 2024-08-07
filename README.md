# Aerofit Descriptive Statistics & Probability Analysis

## Objective
The objective of this project is to perform descriptive statistics and probability analysis on the Aerofit dataset. This analysis helps in understanding the relationship between variables like Age, Gender, Education, Marital Status, Usage, Fitness, Income, and Miles.

## Dataset Information
- **Product:** Type of product purchased.
- **Age:** Age of the customer.
- **Gender:** Gender of the customer.
- **Education:** Number of years of education.
- **Marital Status:** Marital status of the customer.
- **Usage:** Usage of the product.
- **Fitness:** Self-reported fitness score.
- **Income:** Annual income of the customer.
- **Miles:** Number of miles the customer expects to run.

## Data Preprocessing
1. **Loading Data:** Load the dataset using pandas.
2. **Data Cleaning:** Handle missing values and outliers.
3. **Data Transformation:** Create new features like income categories and age categories.

## Exploratory Data Analysis
1. **Descriptive Statistics:**
    - Summary statistics for numerical and categorical columns.
    - Value counts for categorical columns.

2. **Visualizations:**
    - Box plots to visualize distribution and outliers.
    - Bar plots to show relationships between categorical variables.
    - Cross-tabulations to understand distribution across different variables.

## Probability Analysis
1. **Binomial Distribution:** 
    - Analysis of fitness scores based on gender and marital status.
2. **Normal Distribution:**
    - Analysis of income distribution and creation of income categories.

## Achievements
- **Data Cleaning and Preparation:** Successfully handled missing values and outliers.
- **Descriptive Statistics:** Provided detailed insights into the dataset using summary statistics.
- **Visualizations:** Created various visualizations to understand relationships between variables.
- **Probability Analysis:** Applied binomial and normal distributions to analyze fitness scores and income.

## Tools and Libraries
- **Python:** Programming language used.
- **Pandas:** For data manipulation and analysis.
- **NumPy:** For numerical operations.
- **Seaborn:** For statistical data visualization.
- **Matplotlib:** For plotting graphs.
- **Scipy:** For scientific and technical computing.

## Files
- `aerofit_statistics_probability.py`: Python script for performing descriptive statistics and probability analysis on the Aerofit dataset.

## Installation
Ensure the following Python libraries are installed:

```sh
pip install pandas numpy matplotlib seaborn scipy
```


## How to Use
### Clone the Repository:

git clone https://github.com/yourusername/Aerofit-Descriptive-Statistics-Probability.git

### Navigate to the Project Directory:
```sh
cd Aerofit-Descriptive-Statistics-Probability
```

### Install the Required Libraries:
```sh
pip install -r requirements.txt
```

### Run the Analysis:
Open the Python script aerofit_statistics_probability.py and run it to see the analysis.

## Results
The script generates statistical summaries and probability calculations, along with visualizations. Check the console output and plots for detailed insights.
![image](https://github.com/user-attachments/assets/ef067d5a-4cc6-43b9-9d23-6867ff970a88)
![image](https://github.com/user-attachments/assets/7cbc23ac-378e-40cc-80d4-8238dd657612)
![image](https://github.com/user-attachments/assets/52551493-076a-44d1-b1de-ab5616734941)

Gender     Female      Male       All
Product                              
KP281    0.222222  0.222222  0.444444
KP481    0.161111  0.172222  0.333333
KP781    0.038889  0.183333  0.222222
All      0.422222  0.577778  1.000000
Gender    Female      Male       All
Miles                               
21      0.005556  0.000000  0.005556
38      0.016667  0.000000  0.016667
42      0.005556  0.016667  0.022222
47      0.022222  0.027778  0.050000
53      0.011111  0.027778  0.038889
56      0.022222  0.011111  0.033333
64      0.016667  0.016667  0.033333
66      0.044444  0.011111  0.055556
74      0.016667  0.000000  0.016667
75      0.033333  0.022222  0.055556
80      0.000000  0.005556  0.005556
85      0.072222  0.077778  0.150000
94      0.022222  0.022222  0.044444
95      0.022222  0.044444  0.066667
100     0.011111  0.027778  0.038889
Gender    Female      Male       All
Miles                               
260     0.000000  0.005556  0.005556
280     0.005556  0.000000  0.005556
300     0.000000  0.005556  0.005556
360     0.000000  0.005556  0.005556
All     0.422222  0.577778  1.000000
Usage       2   3   4   5  6  7  All
Education                           
12          1   1   1   0  0  0    3
13          0   2   3   0  0  0    5
14         15  28   9   2  0  1   55
15          3   1   0   1  0  0    5
16         13  34  29   7  2  0   85
18          1   3   7   7  4  1   23
20          0   0   1   0  0  0    1
21          0   0   2   0  1  0    3
All        33  69  52  17  7  2  180



## Conclusion
This project provides a comprehensive analysis of the Aerofit dataset, utilizing descriptive statistics and probability analysis. The insights gained from this analysis can help in understanding customer behavior and preferences.
