## Predict who will attend Tour de France
_Jakob Hutter_ - _Central European University, Vienna, Austria_ - _3rd December 2023_ - _Project for Introduction to Machine Learning_ - _Professor Petra Kralj Novak_
  
## Abstract
- Goal of this
- Use procyclingstats.com
- scraped this this that
- Datapoints included: all wt riders from 2010-2023, 2023 test data
- suprised regression modelsn, ANN, clasification perform similarly
- Soltion: 75% accuracy, F1 socre imporant for True
- Conclusion: Inaccurate to 
This outcome is not unexpected, due to the time limit this project and the constraint that come with that such as limited time for building, extending scraper, variable consideration and preprocessing and model tuning.   
For improvement I would:
1. Consider Time-Series Forecasting, this includes understanding how riders performance trajectory, age increase, and team affiliation/change can affect this. Possible [Resource1](https://arxiv.org/pdf/1909.07872.pdf), [Resource2](https://content.iospress.com/download/journal-of-sports-analytics/jsa200463?id=journal-of-sports-analytics%2Fjsa200463)
2. Include more detailed data on specialties ranking of each rider. This is possible via procyclingstats, a draft for a scraper that harvests is already built, but would need extra attention for detailed debugging. 
3. consider procycling specific rules  "each team can send 8 riders
per year to the tdf" that can have influence prediction
positively if included.
4. More detailed Preprocessig and Variable analysis, reconfigeration of what data to harvest. Extend resources to other platforms.


