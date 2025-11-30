# Weather Data Analysis Report
**Student Name:** [Chhavi Goyal]
**Course:** Programming for Problem Solving using Python
**Date:** [30/11/2025]

## 1. Introduction
The objective of this project was to analyze a dataset of daily weather conditions to identify trends in temperature, rainfall, and humidity. The analysis was performed using Python libraries including Pandas for data manipulation, NumPy for statistical calculation, and Matplotlib for visualization.

## 2. Data Cleaning Process
The raw dataset contained missing values which were handled as follows:
- **Temperature:** Missing values were filled using the mean temperature of the dataset to maintain statistical distribution.
- **Humidity:** Missing values were filled using 'forward fill' (carrying forward the previous day's value), assuming weather continuity.
- **Rainfall:** Missing values were assumed to be 0.0 mm.
- **Date Formatting:** The 'Date' column was successfully converted to datetime objects to allow for time-series plotting.

## 3. Statistical Insights
Based on the analysis of the dataset, the following statistics were observed:

### Temperature Analysis
- **Average Temperature:** 21.86°C
- **Maximum Temperature:** 34.67°C
- **Minimum Temperature:** 10.14°C
- **Volatility:** The standard deviation of 7.10 indicates significant fluctuation in daily temperatures during the observed period.

### Rainfall Analysis
- **Total Rainfall:** 610.00 mm
- **Heaviest Rain:** The maximum rainfall recorded in a single day was 20.00 mm.

### Monthly Trends
Grouping the data by month revealed the following averages:
- **February** appeared to be the warmest month on average (22.46°C).
- **January** saw the highest average rainfall intensity (approx 7.58 mm/day).
- **April** had the lowest average humidity (58.82%), suggesting a drier season.

## 4. Visualizations
Three visualizations were generated to support these findings:
1. **Temperature Trends:** A line graph showing the fluctuation of daily temperatures.
2. **Humidity vs. Temperature:** A scatter plot analyzing the correlation between heat and moisture.
3. **Combined Metrics:** A subplot visualizing temperature and rainfall side-by-side.

## 5. Conclusion
The analysis successfully processed the raw weather data. The automated cleaning pipeline ensured no data was lost, and the statistical summary provides a clear overview of the local climate conditions for the recorded period.
