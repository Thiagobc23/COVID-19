# CBC News Articles
An analysis of over [3,500 CBC articles](https://www.kaggle.com/ryanxjhan/cbc-news-coronavirus-articles-march-26) about the COVID-19 pandemic.  
  
Most mentioned words in the titles:  
![titles](https://i.imgur.com/3TU5JZZ.png)
  
I've used VADER to analyze the sentiment polarity of those articles, it uses a dictionary to assign scores to the words while considering their location within the text, punctuations, and other grammatical variables to score the document with a proportion of each sentiment polarity contained on it. Those polarities are classified as negative, positive and neutral.  
  
![polarity_month](https://i.imgur.com/w5Oup3q.png)
  
The values of the polarity score are more spread through time, but we can look even closer to those scores.  

Non-neutral scores - Weekly:  
![polarity_week](https://i.imgur.com/FBXPlp4.png)  
  
Now we can start to see a trend of more positive articles. To extrapolate on that we can normalize the scores within the weeks and have a better look at how they compare against each other.  
  
Normalized non-neutral scores - Weekly:  
![norm_polarity_week](https://i.imgur.com/RwvmCPu.png)  
  
_____
# Restaurant Reservations

Year over year change in restaurant reservations, [data from OpenTable](https://www.kaggle.com/roche-data-science-coalition/uncover) 
![img](https://i.imgur.com/qmJNfx0.gif)
  
_____
# Wellcome Survey - Science Perception
  
The [wellcome global monitor survey](https://wellcome.ac.uk/reports/wellcome-global-monitor/2018) has some very interesting data on public perception over science, medicine, government, and many other topics.
  
Those can be used to understand policies, public responses, and other aspects of the crisis. * Data from 2018

Some examples:  
![img](https://i.imgur.com/FEd9VYw.png)  
  
![img](https://i.imgur.com/fNLHVuM.png)  
  
![img](https://i.imgur.com/bMYmQ3u.png)  
  
_____