## Predicting Tour de France Participation
### Leveraging Data Mining and Public Sources for Strategic Cycling Team Insights
_Jakob Hutter_ - _Central European University, Vienna, Austria_ - _3rd December 2023_ - _Project for Introduction to Machine Learning_ - _Professor Petra Kralj Novak_
  
### Abstract

Cycling teams employ data mining techniques to refine their strategies. This project investigated whether publicly available data from [procyclingstats](https://procyclingstats.com) can be used to predict the cyclists who will participate in the upcoming Tour de France. An accurate prediction tool could allow teams to foresee the line-ups of competitors, providing a strategic edge.

Data was collected from world tour teams (2010-2023) through web scraping, focusing on the 2023 season for model testing. Variables considered included team, age for the season, height, weight, PCS points up to the Tour de France (TdF), UCI points up to TdF, race days until TdF, Giro participation, last season's PCS points, and last season's UCI points. The analysis revealed that pre-season PCS points, a metric indicating strong climbing abilities, were the most significant predictor of TdF participation. Data from January to June of the current season, though important, were less predictive.

The developed model achieved a 75% accuracy and a 61% F1-Score for predicting TdF attendance in the test set. Given the constraints of time, data, and expertise in this project, these results were anticipated. However, the model's accuracy is deemed insufficient for practical applications in predicting team strategies. For enhancing the model, the following improvements are suggested:

1. Implementing time-series forecasting to account for riders' performance trajectories, age progression, and team changes. This approach would require expanding the database to include historical race participation data. Suggested resources include [Resource1](https://arxiv.org/pdf/1909.07872.pdf) and [Resource2](https://content.iospress.com/download/journal-of-sports-analytics/jsa200463?id=journal-of-sports-analytics%2Fjsa200463).

2. Incorporating more detailed data on each rider's specialty rankings, available through procyclingstats.com. A draft scraper has been developed but requires further refinement and debugging.

3. Considering specific rules of pro cycling, such as each team being allowed to send only eight riders to the TdF, which could enhance the prediction accuracy.

4. Improving data preprocessing and variable analysis, reevaluating the data collection approach, and expanding the scope to include other platforms. This could include calculating an pre-season in-team ranking.

This project represents an initial step towards using data analytics in cycling strategy, and these proposed improvements could significantly enhance its practical application.

### Quick Links
1. [Webscraper](https://github.com/jakthehut/predicting_tdf_attendance/tree/main/webscraper)
2. [Data Preprocessing and Manipulation](https://github.com/jakthehut/predicting_tdf_attendance/tree/main/data_manipulation_preprocessing)
3. [Model Traning, Experimentation and Evaluation](https://github.com/jakthehut/predicting_tdf_attendance/tree/main/analysis)
4. [Data](https://github.com/jakthehut/predicting_tdf_attendance/tree/main/data)

