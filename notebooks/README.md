
### Notebook Overview

This repository contains notebooks and codes related to news correlation analysis for the given task. Below are some of the key functions available in the notebooks and codes:

### Functions:

1. **EDA Analysis Functions**:
   - `top_bottom_websites()`: Analyzes and returns the top and bottom 10 websites based on various criteria such as news article count, visitor traffic, etc.
   - `country_analysis()`: Performs analysis to identify countries with the highest number of news media organizations and those with many articles written about them.

2. **Sentiment Analysis Functions**:
   - `sentiment_counts_by_domain()`: Groups the data by website domain and calculates the count of positive, neutral, and negative sentiment articles.
   - `compare_sentiment_impact()`: Compares the impact of using mean/average and median sentiment.

3. **Visualization Functions**:
   - `scatter_plot_total_reports()`: Generates a 2D scatter plot with the total number of reports by a website on the x-axis and the global ranking of the site on the y-axis. Color represents average/median sentiment.

4. **Data Processing Functions**:
   - `calculate_average_sentiment()`: Calculates the average sentiment for each domain and approximates it to one of the three categories (positive, neutral, negative).

5. **Git Integration Functions**:
   - `push_to_git()`: Integrates with Git to push changes to a specified branch in the repository.

---

These functions are designed to facilitate data exploration, analysis, visualization, and version control within the context of news correlation analysis. They provide essential functionality to conduct meaningful analysis and draw insights from the data.

Please refer to the respective notebooks and code files for more detailed documentation and usage instructions of each function.
