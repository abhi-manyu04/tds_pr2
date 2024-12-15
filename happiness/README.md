
# happiness.csv

## Dataset Overview
The `happiness.csv` dataset contains valuable insights into the well-being of individuals across various countries over different years. The dataset consists of the following columns:

- **Country name**: The name of the country.
- **year**: The year the data was collected.
- **Life Ladder**: An index that reflects the perceived quality of life.
- **Log GDP per capita**: The natural logarithm of income per capita, a direct measure of economic wealth.
- **Social support**: An index that measures the support individuals can count on from their social circle.
- **Healthy life expectancy at birth**: The average number of years a person can expect to live in good health.
- **Freedom to make life choices**: An index indicating the degree of freedom individuals perceive in making life decisions.
- **Generosity**: Measures the tendency of individuals to give to others, reflected as an index.
- **Perceptions of corruption**: Indicates the level at which corruption is perceived in a country.
- **Positive affect**: A measure of positive emotions experienced by individuals.
- **Negative affect**: A measure of negative emotions experienced by individuals.

### Recommended Analysis
- Correlating GDP per capita with the Life Ladder score to investigate the impact of economic wealth on happiness.
- Analyzing the relationship between social support and both positive and negative affect to understand emotional well-being.
- Examining outliers in various features to identify unique trends and anomalies in the happiness landscape across countries.

## Number of Samples and Features
The dataset contains a total of **2363 samples** and **11 features**. Here’s a quick summary of the descriptive statistics for each column:

| Column                                      | Count   | Unique | Top           | Frequency | Mean       | Standard Deviation | Min  | 25%   | 50%   | 75%   | Max  |
|---------------------------------------------|---------|--------|---------------|-----------|------------|---------------------|------|-------|-------|-------|------|
| Country name                                | 2363    | 165    | Argentina     | 18        | N/A        | N/A                 | N/A  | N/A   | N/A   | N/A   | N/A  |
| year                                        | 2363    | N/A    | N/A           | N/A       | 2014.76    | 5.06                | 2005 | 2011  | 2015  | 2019  | 2023 |
| Life Ladder                                 | 2363    | N/A    | N/A           | N/A       | N/A        | N/A                 | N/A  | N/A   | N/A   | N/A   | N/A  |
| Log GDP per capita                          | 2335    | N/A    | N/A           | N/A       | N/A        | N/A                 | N/A  | N/A   | N/A   | N/A   | N/A  |
| Social support                              | 2350    | N/A    | N/A           | N/A       | N/A        | N/A                 | N/A  | N/A   | N/A   | N/A   | N/A  |
| Healthy life expectancy at birth            | 2300    | N/A    | N/A           | N/A       | N/A        | N/A                 | N/A  | N/A   | N/A   | N/A   | N/A  |
| Freedom to make life choices                | 2327    | N/A    | N/A           | N/A       | N/A        | N/A                 | N/A  | N/A   | N/A   | N/A   | N/A  |
| Generosity                                  | 2282    | N/A    | N/A           | N/A       | N/A        | N/A                 | N/A  | N/A   | N/A   | N/A   | N/A  |
| Perceptions of corruption                    | 2238    | N/A    | N/A           | N/A       | N/A        | N/A                 | N/A  | N/A   | N/A   | N/A   | N/A  |
| Positive affect                             | 2339    | N/A    | N/A           | N/A       | 0.6519     | 0.1062              | 0.179| 0.572 | 0.663 | 0.737 | 0.884|
| Negative affect                             | 2347    | N/A    | N/A           | N/A       | 0.2732     | 0.0871              | 0.083| 0.209 | 0.262 | 0.326 | 0.705|

## Column Details
Here’s a brief overview of each column and some interesting value counts:

1. **Country name**:
   - Unique countries: 165
   - Most frequent: Argentina (18 occurrences).
  
2. **year**:
   - Range of years: 2005 to 2023.
   - Most common year: 2017 (147 occurrences).

3. **Life Ladder**:
   - Significant values range across the dataset with 5.252 being the least common.

4. **Log GDP per capita**:
   - Missing values: 28
  
5. **Social support**:
   - Missing values: 13

6. **Healthy life expectancy at birth**:
   - Missing values: 63

7. **Freedom to make life choices**:
   - Missing values: 36

8. **Generosity**:
   - Missing values: 81

9. **Perceptions of corruption**:
   - Missing values: 125 

10. **Positive affect**:
    - Missing values: 24 

11. **Negative affect**:
    - Missing values: 16 

## Key Insights and Next Steps
The `happiness.csv` dataset reveals intriguing patterns and outliers that can significantly impact our understanding of global happiness. Some notable findings include:
- **Outliers**: 
  - Life Ladder has 2 outliers. 
  - Log GDP per capita has 1 outlier. 
  - Social support has 48 outliers. 
  - Healthy life expectancy at birth has 20 outliers. 
  - Freedom to make life choices has 16 outliers. 
  - Generosity has 39 outliers. 
  - Perceptions of corruption has a staggering 194 outliers. 
  - Positive affect has 9 outliers. 
  - Negative affect has 31 outliers. 

Next steps could involve cleaning the dataset for these outliers and conducting a series of visualizations and statistical analyses to uncover deeper insights into the relationships between happiness and its indicators across the globe. Engage with this dataset and be a part of the exploration to understand what truly defines happiness!
