# Exploratory Data Analysis (EDA) Summary

## Project Planning - EDA & Stats

### CRISP-DM Framework
In this notebook, we follow the CRISP-DM (Cross-Industry Standard Process for Data Mining) framework, which consists of six phases: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment. Our focus lies primarily on the Data Understanding and Exploratory Data Analysis (EDA) phases.

### Data Understanding
We start by understanding our dataset, which contains news articles from various websites. We explore key attributes such as source name, domain, traffic ranks, sentiment analysis, content metadata, and more. Understanding these attributes helps us formulate relevant questions and hypotheses for further analysis.

### Exploratory Data Analysis (EDA)
EDA is crucial for gaining insights into the dataset, identifying patterns, and understanding relationships between variables. Throughout the analysis, we perform various tasks to answer specific questions and explore different aspects of the data.

### Statistical Thinking
Statistical thinking is applied to uncover patterns, trends, and relationships within the data. Descriptive statistics such as mean, median, variance, and distribution analysis help us understand the characteristics of the dataset.

## Key Exploration Points

### Top and Bottom 10 Websites
We identify the top and bottom 10 websites based on the count of news articles they have reported.

### Websites with the Highest Traffic
We determine the websites with the highest traffic by examining their global traffic ranks.

### Countries with the Most News Media Organizations
We analyze the domains to identify the countries with the highest number of news media organizations represented.

### Countries with Many Articles Written About Them
We group countries together to determine which ones have many news articles written about them.

### Sentiment Analysis
We conduct sentiment analysis by grouping data by website domain and calculating descriptive statistics such as mean, median, and variance for positive, neutral, and negative sentiment.

### Comparison of Mean/Average and Median Sentiment
We compare the impact of using mean/average and median for sentiment analysis.

### Distribution of Sentiments for Top Domains
We analyze the distribution of sentiments for the top 10 domains by visitor traffic and compare it with the global news sentiment distribution.

### Comparison of Content Metadata Across Sites
We compare raw message lengths and the number of words in titles across different websites to understand similarities and differences.

### Impact of News Reporting and Sentiment on Global Ranking
We explore the relationship between frequent news reporting, sentiment, and website global ranking using a 2D scatter plot. The x-axis represents the total number of reports by a website, the y-axis represents the global ranking of the site, and the color represents average/median sentiment.

## Conclusion
Through EDA, we gain valuable insights into the dataset, uncover patterns, and understand the factors influencing news reporting, sentiment, and website ranking. This analysis forms the basis for further exploration and modeling to extract actionable insights and make informed decisions.
