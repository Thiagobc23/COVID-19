# Objective

To report, analyze, visualize, and acquire knowledge of the current Corona Virus Disease 2019 (COVID-19).  
  
# Visualizations  
  

[World Map - Time series/ Animated](https://imgur.com/LSKZUTn)  
![World Map, 01-04-2020](https://i.imgur.com/2XsW5Gn.png)   
  
[Confirmed Cases - Time series/ Animated](https://imgur.com/j8a3AU2)
![Confirmed Cases, 01-04-2020](https://i.imgur.com/yh0TCWP.png)
  
## Most Affected  
Total confirmed cases after 500 cases, Most affected countries:
![Confirmed Cases](https://i.imgur.com/mrxktml.png)  
![Mortality](https://i.imgur.com/aJRyNr8.png)  
![Recovered](https://i.imgur.com/RVpd3SW.png)  
  
The most affected countries in their regions:  
China, Asia/ Italy, Europe/ U.S., North America.  
  
*Until 30-03-2020, they were also the most affected countries in the world.  
  
 
  
**Italy** is the second country to have extremely high numbers of infections, it started after China's lockdown and quarantine procedures while WHO was telling the situation was under control. Since they were the first country to be heavily hit after China, their healthcare system couldn't handle the situation and was quickly overwhelmed by cases. Italy is, for now, the country with the most registered casualties and motivated most of the world to act in preparation for the COVID-19 pandemic.

**United States** is currently the country with most cases, it started to accumulate cases really soon, but only recognized the problem on the late march when the many epidemics spread trought the country couldn't be contained anymore. Most of the mistakes the US committed were due to poor leadership and denialism of what was happening. Apparently they recently realized the impacts this crisis will bring to the economy and began to heavily test and prepare for the ongoing crisis.
  
[Trump on COVID-19](https://twitter.com/i/status/1242193904553865216)
  
**Spain** was heavily hit with the virus shortly after Italy, they are currently the third country with most cases of the disease and the second country with the most fatalities.  
  
_____

## Most Affected (Europe)
The most affected countries so far are Italy, Spain, Germany, UK, and France.  
  
Total confirmed cases after 500 cases, Most affected countries (Europe):
![Confirmed Cases](https://i.imgur.com/1oSsboZ.png)
![Mortality](https://i.imgur.com/zVpF2sg.png)
![Recovered](https://i.imgur.com/JzRfjt3.png)
  
**Germany** apparently has been handling well the situation, they started to the crisis with very high amounts of testings and even though this made their numbers increase quite fast they're apparently aware of the situation and are being able to maintain a very low mortality rate. They are also the only country I've heard so far to be helping other EU countries with not only resources but also taking [patients for treatment](https://www.foxnews.com/world/germany-takes-coronavirus-patients-from-italy).  
  
## Personal Selection
Besides the most affected countries, I want to keep track of Canada which is the country I'm currently living, South Korea which is an example of how to properly deal with the epidemic and has a track record of transparent release of data and information, and Brazil which is my home country and apparently is about to become some kind of control group for a very bizarre experiment of what happens when you simply let the virus spread, Brazil also has issues within its data collection, mostly for lack of testing so the information is not completely trustworthy.  
  
![Confirmed Cases](https://i.imgur.com/CbiwZe1.png)  
![Mortality](https://i.imgur.com/oR1MiW6.png)
![Recovered](https://i.imgur.com/4umKYx6.png)
  
_____
  
## China
  
![Confirmed Cases](https://i.imgur.com/k4SW8Ar.png)  

**China** is the epicenter of the disease, where it originated and started spreading. It has been keeping a very bad record of the epidemic, with [misleading data](https://www.forbes.com/sites/kenrapoza/2020/03/31/china-hints-that-its-coronavirus-data-doesnt-paint-full-picture/#59d700422d58), reluctancy to accept the situation and [poor handling of the medical team](https://www.theguardian.com/world/2020/mar/11/coronavirus-wuhan-doctor-ai-fen-speaks-out-against-authorities) that both discovered and are treating the pandemic. In addition to that, at the start of the pandemic [WHO supported China](https://nationalpost.com/news/world/this-is-not-a-time-for-fear-who-downplays-criticism-china-hushed-up-coronavirus-in-early-days) to [hide the actual numbers](https://www.cnbc.com/2020/04/01/coronavirus-china-hid-extent-of-outbreak-us-intelligence-reportedly-says.html?view=story) and misdirect world efforts by ensuring other nations that China was doing a great job containing the virus. This series of misleading actions and grave mistakes led to the second extremely hit country, Italy.  
  
![WHO Tweet](https://i.imgur.com/vndyBbH.png)
  
[Late Asymptomatic Cases Reporting](https://www.cnn.com/2020/03/31/asia/china-asymptomatic-coronavirus-cases/index.html) 
  
![Mortality](https://i.imgur.com/z6nHw17.png)  
![Recovered](https://i.imgur.com/j9kX54e.png)  

_____

## Regressions

Those regressions are based on the work compiled by [Xingyu Bian](https://www.kaggle.com/therealcyberlord/coronavirus-covid-19-visualization-prediction).  
  
It's important to make a few notes about regressions and predictions at this time, those numbers are for illustration and research only and should never replace any kind of medical or governmental information you may receive. It's also important to note that the veracity of the analyzed data is questionable so predictions may have a huge distortion when compared to reality.
  
SVM - Support Vector Machine Regressor:  
![svm](https://i.imgur.com/buFEWdL.png)
  
    SVM future predictions:
    {('04/02/2020', 889598.0),
    ('04/03/2020', 963770.0),
    ('04/04/2020', 1043277.0),
    ('04/05/2020', 1128419.0),
    ('04/06/2020', 1219513.0),
    ('04/07/2020', 1316887.0),
    ('04/08/2020', 1420882.0),
    ('04/09/2020', 1531853.0),
    ('04/10/2020', 1650171.0),
    ('04/11/2020', 1776219.0)}
  
Polynomial Regression:  
![Pol_reg](https://i.imgur.com/WJw3wCF.png)
  
    Polynomial regression future predictions:
    {('04/02/2020', 1112583.0),
    ('04/03/2020', 1230595.0),
    ('04/04/2020', 1358990.0),
    ('04/05/2020', 1498414.0),
    ('04/06/2020', 1649536.0),
    ('04/07/2020', 1813052.0),
    ('04/08/2020', 1989681.0),
    ('04/09/2020', 2180172.0),
    ('04/10/2020', 2385297.0),
    ('04/11/2020', 2605858.0)}
  
Polynomial Baysian Ridge Regression:  
![Pol_Bay_Rid](https://i.imgur.com/n3ju0AL.png)  
  
    Ridge regression future predictions:
    {('04/02/2020', 851510.0),
    ('04/03/2020', 913161.0),
    ('04/04/2020', 978333.0),
    ('04/05/2020', 1047174.0),
    ('04/06/2020', 1119837.0),
    ('04/07/2020', 1196479.0),
    ('04/08/2020', 1277260.0),
    ('04/09/2020', 1362347.0),
    ('04/10/2020', 1451909.0),
    ('04/11/2020', 1546121.0)}
  
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

_____
## CBC News Articles
An analysis of over [3,500 CBC articles](https://www.kaggle.com/ryanxjhan/cbc-news-coronavirus-articles-march-26) about the COVID-19 pandemic.  
  
Most mentioned words in titles:  
![titles](https://i.imgur.com/3TU5JZZ.png)
  
I've used VADER to analyse the sentiment polarity of those articles, VADER uses a dictionary to assign scores to the words, while considering their location within the text and punctuations to score the document with a proportion of each sentiment contained on it. Those sentiments are named negative, positive and neutral.  
  
After getting the proportions for each sentiment VADER calculates a compound. The compound is a normalized sum of all proportions, from -1 (completely negative) to 1 (completely positive).  
  
Some of the semantic contexts considered by VADER are:  
  
        Conjunctions	    E.g.: 'I like your X, but your Y is very bad';
        Negation Flips 	    E.g.: 'This is not really the greatest';
        Degrees		    E.g.: 'This is good' vs 'This is extremely good';
        Capitalization 	    E.g.: 'this is GREAT' vs 'this is great';
        Punctuation		    E.g.: 'this is great!!!' vs 'this is great'; 
  
Overall Polarity:  
![Overall](https://i.imgur.com/Qrt9Tsj.png)
  
Most of a text polarity is usualy neutral, so this results are not surprising. There are other ways of looking at sentiment polarity, rather than an overall score, let's start by grouping the values.

Monthly:  
![polarity_month](https://i.imgur.com/w5Oup3q.png)
  
Now we can see that the spread of the polarity score is spreading through time, but we can look even closer to those scores.  

Non-neutral scores - Weekly:  
![polarity_week](https://i.imgur.com/FBXPlp4.png)  
  
Now we can start to see a trend of more positive articles. To extrapolate on that we can normalize the scores within the weeks and have a better look at how they compare against each other.  
  
Normalized-neutral scores - Weekly:  
![norm_polarity_week](https://i.imgur.com/RwvmCPu.png)  
  
# References, resources, and inspirations.  
  
Kaggle Covid-19 research effort:  
[Forecast competition w1](https://www.kaggle.com/c/covid19-global-forecasting-week-1);  
[Forecast competition w2](https://www.kaggle.com/c/covid19-global-forecasting-week-2);  
[Research Papers](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge/);  
  
Data:  
[Daily Cases and Reports - by Johns Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19)
[CBC News Articles Dataset](https://www.kaggle.com/ryanxjhan/cbc-news-coronavirus-articles-march-26)  
[Data Science for Covid-19 - South Korea Data](https://www.kaggle.com/kimjihoo/coronavirusdataset)  
[Daily Cases Report](https://www.kaggle.com/imdevskp/corona-virus-report);  
  
Other Researches, Papers, and Publications:  
[Economics in the Time of COVID-19](http://viet-studies.net/kinhte/COVID19_CPER.pdf), edited by Richard Baldwin and Beatrice Weder di Mauro.  
[Economic Strategy Group Statement - COVID-19](https://economicstrategygroup.org/resource/economic-strategy-group-statement-covid19/)  
  

### More Info About this Project:
For now, I'm just collecting and analyzing data. As things are way too fast I'm not properly documenting my code or explaining what I'm doing, but I do want to revisit this project and complete it properly.
