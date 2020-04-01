# Objective

To report, analyze, visualize, and acquire knowledge of the current Corona Virus Disease 2019 (COVID-19).  
  
# Visualizations  
  

[World Map - Time series/ Animated](https://imgur.com/aom2R1j)  
![World Map, 31-03-2020](https://i.imgur.com/tM2cN2h.png)   
  
[Confirmed Cases - Time series/ Animated](https://imgur.com/eCGfx3w)
![Confirmed Cases, 31-03-2020](https://i.imgur.com/fjzXLAA.png)
  
## Most Affected  
Total confirmed cases after 500 cases, Most affected countries:
![Confirmed Cases](https://i.imgur.com/DnoMq7e.png)  
![Mortality](https://i.imgur.com/NwiL5TF.png)  
  
The most affected countries so far are China, the U.S., and Italy.

**China** is the epicenter of the disease, where it originated and started spreading. It has been keeping a very bad record of the epidemic, with misleading data, reluctancy to accept the situation and poor handling of the medical team that both discovered and are treating the pandemic. In addition to that, at the start of the pandemic WHO supported China to hide the actual numbers and misdirect world efforts by ensuring other nations that China was doing a great job containing the virus. This series of misleading actions and grave mistakes led us to the second hit country.  
  
![WHO Tweet](https://i.imgur.com/vndyBbH.png)


**Italy** is the second country to have extremely high numbers of infections, it started after China's lockdown and quarantine procedures while WHO was telling the world the situation was under control. Since they were the first country to be heavily hit after China, their healthcare system couldn't handle the situation and was quickly overwhelmed by cases. Italy is, for now, the country with the most registered casualties and motivated most of the world to act in preparation for the COVID-19 pandemic.

**United States** is currently the country with most cases, it started to accumulate cases really soon, but only recognized the problem on the late march when the many epidemics spread trought the country couldn't be contained anymore. Most of the mistakes the US committed were due to poor leadership and denialism of what was happening. Apparently they recently realized the impacts this crisis will bring to the economy and began to heavily test and prepare for the ongoing crisis.
  
[Trump on COVID-19](https://twitter.com/i/status/1242193904553865216)
  
## Most Affected (Europe)
The most affected countries so far are Italy, Spain, and Germany.

Total confirmed cases after 500 cases, Most affected countries (Europe):
![Confirmed Cases](https://i.imgur.com/z7FJF28.png)
![Mortality](https://i.imgur.com/P0evP06.png)
  
## Personal Selection
Besides the most affected countries, I want to keep track of Canada which is the country I'm currently living, South Korea which is an example of how to properly deal with the epidemic and has a track record of transparent release of data and information, and Brazil which is my home country and apparently is about to become some kind of control group for a very bizarre experiment of what happens when you simply let the virus spread, Brazil also has issues within its data collection, mostly for lack of testing so the information is not completely trustworthy.  
  
![Confirmed Cases](https://i.imgur.com/q94HRy4.png)  
![Mortality](https://i.imgur.com/4nMaz7P.png)
  
_____
  
## Regressions

Those regressions are based on the work compiled by [Xingyu Bian](https://www.kaggle.com/therealcyberlord/coronavirus-covid-19-visualization-prediction).  
  
It's important to make a few notes about regressions and predictions at this time, those numbers are for illustration and research only and should never replace any kind of medical or governmental information you may receive. It's also important to note that the veracity of the analyzed data is questionable so predictions may have a huge distortion when compared to reality.
  
SVM - Support Vector Machine Regressor:  
![svm](https://i.imgur.com/qDUGJhO.png)
  
    SVM future predictions:
    {('04/01/2020', 969732.0),
    ('04/02/2020', 1077730.0),
    ('04/03/2020', 1196916.0),
    ('04/04/2020', 1328271.0),
    ('04/05/2020', 1472844.0),
    ('04/06/2020', 1631759.0),
    ('04/07/2020', 1806220.0),
    ('04/08/2020', 1997512.0),
    ('04/09/2020', 2207007.0),
    ('04/10/2020', 2436171.0)}


Polynomial Regression:  
![Pol_reg](https://i.imgur.com/8hsCz8r.png)
  
    Polynomial regression future predictions:
    {('04/01/2020', 1029636.0),
    ('04/02/2020', 1146995.0),
    ('04/03/2020', 1276148.0),
    ('04/04/2020', 1418012.0),
    ('04/05/2020', 1573553.0),
    ('04/06/2020', 1743795.0),
    ('04/07/2020', 1929815.0),
    ('04/08/2020', 2132748.0),
    ('04/09/2020', 2353791.0),
    ('04/10/2020', 2594202.0)}

Polynomial Baysian Ridge Regression:  
![Pol_Bay_Rid](https://i.imgur.com/Mb68RwC.png)  
  
    Ridge regression future predictions:
    {('04/01/2020', 1175073.0),
    ('04/02/2020', 1333592.0),
    ('04/03/2020', 1511025.0),
    ('04/04/2020', 1709069.0),
    ('04/05/2020', 1929525.0),
    ('04/06/2020', 2174307.0),
    ('04/07/2020', 2445440.0),
    ('04/08/2020', 2745069.0),
    ('04/09/2020', 3075461.0),
    ('04/10/2020', 3439010.0)}


_____
  
## Patients Info (Based on a sample of [South Korea Cases](https://www.kaggle.com/kimjihoo/coronavirusdataset))  
  
Age Distribution - All Patients  
![Age Distribution - All Patients](https://i.imgur.com/ipzbgn1.png)  
Age Distribution - Female Patients  
![Age Distribution - Female Patients](https://i.imgur.com/ndugyO7.png)  
Age Distribution - Male Patients  
![Age Distribution - Male Patients](https://i.imgur.com/F351lOa.png)  
Age Distribution - Released Patients  
![Age Distribution - Released Patients](https://i.imgur.com/torXsJ3.png)  
Age Distribution - Deceased Patients  
![Age Distribution - Deceased Patients](https://i.imgur.com/uYZLVVn.png)  

Histogram of patients by days until release  
(days between confirmed case and release)  
  
![All](https://i.imgur.com/20E3zk9.png)  
![29](https://i.imgur.com/diVe6Ty.png)  
![59](https://i.imgur.com/V5V9PIk.png)  
![60plus](https://i.imgur.com/kBEJWZi.png)  

Histogram of patients by days until fatality  
(days between the confirmed case and deceased date)  

![All](https://i.imgur.com/A1GWMXl.png)

![60plus](https://i.imgur.com/HqnHsSx.png)  


# Resources  
  
Kaggle Covid-19 research effort:  
[Forecast competition w1](https://www.kaggle.com/c/covid19-global-forecasting-week-1);  
[Forecast competition w2](https://www.kaggle.com/c/covid19-global-forecasting-week-2);  
[Research Papers](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/);  
[Daily Cases Report](https://www.kaggle.com/imdevskp/corona-virus-report);  
[Data Science for Covid-19](https://www.kaggle.com/kimjihoo/coronavirusdataset);  
  
Data:  
[Daily Cases and Reports](https://github.com/CSSEGISandData/COVID-19)
  
Other Researches, Papers, and Publications:  
[Economics in the Time of COVID-19](http://viet-studies.net/kinhte/COVID19_CPER.pdf), edited by Richard Baldwin and Beatrice Weder di Mauro.  
[Economic Strategy Group Statement - COVID-19](https://economicstrategygroup.org/resource/economic-strategy-group-statement-covid19/)  
  

### More Info About this Project:
For now, I'm just collecting and analyzing data. As things are way too fast I'm not properly documenting my code or explaining what I'm doing, but I do want to revisit this project and complete it properly.
