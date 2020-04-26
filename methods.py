#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import moviepy.editor as mp
from IPython.display import Video
import imageio

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world[~world.name.isin(["Antarctica", "Fr. S. Antarctic Lands"])]
#PATH = "C:/py/covid19/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
path = 'data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/'

file = '04-25-2020.csv'
today = '04-25-2020'
today = pd.to_datetime(today, format = "%m-%d-%Y")
df = pd.read_csv(path+file)
df.head()


# In[ ]:


# Rank countries by category (confirmed, deaths, recovered)
def plot_rank(col, limit, color):
    df_countries = df.groupby('Country_Region').sum()
    df_countries['Active'] = df_countries['Confirmed'] - df_countries['Recovered'] - df_countries['Deaths']
    
    fig, ax = plt.subplots(1, figsize=(16,8))
 
    rank = df_countries.sort_values(col, ascending=False)
    rank[:limit].sort_values(col).plot(y=col, kind='barh', ax=ax, color=color)

    # grid
    ax.grid(color='grey', linestyle='dashed', linewidth=1, axis = 'x')
    ax.set_axisbelow(True)

    # remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.title(col)
    plt.show()


# plot 20 countries with the most confirmed cases 
# and their number of confimed, active, and deaths
def plot_day(df, i):
    try:
        df_countries = df.groupby('Country_Region').sum()
    except:
        df_countries = df.groupby('Country/Region').sum()
    
    df_countries['Active'] = df_countries['Confirmed'] - df_countries['Recovered'] - df_countries['Deaths']

    fig, ax = plt.subplots(1, figsize=(16,8), facecolor='black')

    rank = df_countries.sort_values('Confirmed', ascending=False)[:20].sort_values('Confirmed', ascending=True)

    rank.plot(y='Deaths', kind='barh', ax=ax, color='grey')

    rank.plot(y='Recovered', kind='barh', ax=ax, color='lightblue', left = rank['Deaths'])

    rank.plot(y='Active', kind='barh', ax=ax, color='orangered', left = (rank['Deaths']+rank['Recovered']))

    # grid
    ax.grid(color='grey', linestyle='dashed', linewidth=1, axis = 'x')
    ax.set_axisbelow(True)

    # remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    #Colors and Sizes
    ax.set_facecolor('xkcd:black')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.ylabel('Countries', fontsize=16)
    plt.legend(fontsize=16)
    
    plt.subplots_adjust(left=0.15, right=1, top=0.95, bottom=0.05)
    
    plt.title(str(i)[:10] + ' | ' + '{:,d}'.format(df['Confirmed'].sum()) +' CONFIRMED CASES',
              color='white', fontsize = 18)   
    
    plt.savefig('img/video/'+str(i)[:10]+'.png', facecolor='black', edgecolor='none')


# plot map of active confirmed and recovered    
def plot_map(df, i):
    fig, ax = plt.subplots(1, figsize=(20,11), facecolor='grey')

    # plot map
    world.plot(ax=ax, color='black')
    
    try:
        # plot infected locations
        df.plot(kind='scatter', x='Long_', y='Lat', ax=ax, color='orangered', 
                s=pd.to_numeric(df['Confirmed'], errors='coerce')/200, alpha=0.8)
        north = df[df['Lat']>0]['Confirmed'].sum()
        south = df[df['Lat']<0]['Confirmed'].sum()
    except:
        # plot infected locations
        df.plot(kind='scatter', x='Longitude', y='Latitude', ax=ax, color='orangered', 
                s=pd.to_numeric(df['Confirmed'], errors='coerce')/200, alpha=0.8)
        north = df[df['Latitude']>0]['Confirmed'].sum()
        south = df[df['Latitude']<0]['Confirmed'].sum()
    plt.legend(['Confirmed'], fontsize = 18)
    
    plt.plot([-180,180], [0,0], color='white', linestyle='dashed', alpha=0.3)
    plt.text(0, 100, str(i)[:10], color = 'black', fontsize = 25, ha='center')
    
    plt.text(0, -60, '{:,d}'.format(df['Confirmed'].sum()), 
             color = 'white', fontsize = 25, ha='center')
    
    plt.text(0, -50, 'CONFIRMED CASES', 
             color = 'white', fontsize = 15, ha='center')



    plt.text(-180, 9, 'Northern Hemisphere', fontsize=16, color = 'white')
    plt.text(-180, 5, '{:,d}'.format(north) + ' cases', 
            fontsize=16, color = 'white')

    plt.text(-180, -5, 'Southern Hemisphere', fontsize=16, color = 'white')
    plt.text(-180, -9, '{:,d}'.format(south) + ' cases', 
            fontsize=16, color = 'white')

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    # hide map axis
    ax.axis('off')
    #ax.legend(['Confirmed','Recovered'], fontsize = 18)
    
    plt.savefig('img/video/'+str(i)[:10]+'_map.png', facecolor='grey', edgecolor='none')


def build_gif(filenames, title, duration=1):
    images = []
    print('Building .gif...')
    for filename in filenames:
        images.append(imageio.imread(filename))
    print('writing .gif...')
    imageio.mimwrite((title + '.gif'), images, duration=duration, loop=1)
    print('concluded')


def build_df(file):

    temp = pd.read_csv(path+file)
    
    try:
        temp = temp.groupby('Country_Region').sum().copy()
    except:
        temp = temp.groupby('Country/Region').sum().copy()
        
    df_new = pd.DataFrame(temp.index)
    df_new.columns = ['Country']

    df_new['Confirmed'] = temp['Confirmed'].values
    df_new['Deaths'] = temp['Deaths'].values
    df_new['Recovered'] = temp['Recovered'].values
    df_new['Active'] = df_new['Confirmed'] - df_new['Deaths'] - df_new['Recovered']
    df_new['Date'] = [file[:10] for i in np.arange(0,len(df_new))]
    return df_new


def get_range(first_file='01-22-2020', start='01-23-2020', end=today):
    start = pd.to_datetime(start, format = "%m-%d-%Y")
    end = pd.to_datetime(end, format = "%m-%d-%Y")

    dates = pd.date_range(start= start, end=end)
    files = []

    for i in dates.strftime('%m-%d-%Y'):
        files.append(str(i)+'.csv')

    df = build_df(first_file+'.csv')

    for file in files:
        #print(file)
        new = build_df(file)
        df = df.append(new, sort=False)

    return df


# confirmed cases
def plot_contry(ax, name, first_file='01-22-2020', start='01-23-2020', end=today, inverse = False):
    start = pd.to_datetime(start, format = "%m-%d-%Y")
    end = pd.to_datetime(end, format = "%m-%d-%Y")
    
    df = get_range(first_file, start, end)
    
    country = df[df['Country'].isin(name)]

    if inverse:
        country = df[~df['Country'].isin(name)]
        country = country.groupby('Date').sum()
    
    x = np.arange(0, len(country))
    plt.plot(x, country.Confirmed, marker='.')
    #plt.scatter(us.Date, us.Confirmed)

    # grid
    ax.grid(color='grey', linestyle='dashed', linewidth=1, axis = 'y')
    ax.set_axisbelow(True)

    # remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    #title
    plt.xticks(x[::5],rotation=45, ha='right', fontsize=12)
    plt.xlabel('Days after 500 cases', fontsize=18)
    plt.title('Confirmed Cases', fontsize=22, color='white')
    
    #Colors
    ax.set_facecolor('xkcd:black')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')


# deaths method 1
def plot_contry_d(ax, name, first_file='01-22-2020', start='01-23-2020', end=today, inverse=False):
    start = pd.to_datetime(start, format = "%m-%d-%Y")
    end = pd.to_datetime(end, format = "%m-%d-%Y")
    
    df = get_range(first_file, start, end)
    
    country = df[df['Country'].isin(name)]
    
    if inverse:
        country = df[~df['Country'].isin(name)]
        country = country.groupby('Date').sum()
    
    x = np.arange(0, len(country))
    plt.plot(x, country.Deaths /country.Confirmed * 100)

    # grid
    ax.grid(color='grey', linestyle='dashed', linewidth=1, axis = 'y')
    ax.set_axisbelow(True)

    # remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    #title
    plt.xticks(x[::10], rotation=45, ha='right')
    plt.title('Deaths/Confirmed', color='white')
    plt.ylabel('%')
    
    ax.set_facecolor('xkcd:black')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')


# Deaths, method 2
def plot_contry_d_two(ax, name, first_file='01-22-2020', start='01-23-2020', end=today, inverse=False):
    start = pd.to_datetime(start, format = "%m-%d-%Y")
    end = pd.to_datetime(end, format = "%m-%d-%Y")
    
    df = get_range(first_file, start, end)
    
    country = df[df['Country'].isin(name)]
    
    if inverse:
        country = df[~df['Country'].isin(name)]
        country = country.groupby('Date').sum()
    
    x = np.arange(0, len(country))
    plt.plot(x, country.Deaths /(country.Recovered+country.Deaths) * 100, linestyle='dashdot')
    #plt.scatter(us.Date, us.Confirmed)
    
    # grid
    ax.grid(color='grey', linestyle='dashed', linewidth=1, axis = 'y')
    ax.set_axisbelow(True)

    # remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    #title
    plt.xticks(x[::10], rotation=45, ha='right')
    plt.title('Deaths/(Deaths+Recovered)', color = 'white')
    plt.ylabel('%')
    
    ax.set_facecolor('xkcd:black')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')


# Recoveries
def plot_contry_r(ax, name, first_file='01-22-2020', start='01-23-2020', end=today, inverse=False):
    start = pd.to_datetime(start, format = "%m-%d-%Y")
    end = pd.to_datetime(end, format = "%m-%d-%Y")
    
    df = get_range(first_file, start, end)    
    country = df[df['Country'].isin(name)]
    
    if inverse:
        country = df[~df['Country'].isin(name)]
        country = country.groupby('Date').sum()
        
    x = np.arange(0, len(country))
    plt.plot(x, country.Recovered /country.Confirmed * 100)
    #plt.scatter(us.Date, us.Confirmed)

    # grid
    ax.grid(color='grey', linestyle='dashed', linewidth=1, axis = 'y')
    ax.set_axisbelow(True)

    # remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    #title
    plt.xticks(x[::5], rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=18)
    plt.title('Recovery Rate', fontsize=18, color='white')
    plt.ylabel('%', fontsize=18)
    plt.xlabel('Days after 500 cases', fontsize=18)
    
    ax.set_facecolor('xkcd:black')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')


# Active 
def plot_contry_a(ax, name, first_file='01-22-2020', start='01-23-2020', end=today, inverse = False):
    start = pd.to_datetime(start, format = "%m-%d-%Y")
    end = pd.to_datetime(end, format = "%m-%d-%Y")
    
    df = get_range(first_file, start, end)
    
    country = df[df['Country'].isin(name)]

    if inverse:
        country = df[~df['Country'].isin(name)]
        country = country.groupby('Date').sum()
    
    x = np.arange(0, len(country))
    plt.plot(x, country.Active, marker='.')
    #plt.scatter(us.Date, us.Confirmed)

    # grid
    ax.grid(color='grey', linestyle='dashed', linewidth=1, axis = 'y')
    ax.set_axisbelow(True)

    # remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    #title
    plt.xticks(x[::5],rotation=45, ha='right', fontsize=12)
    plt.xlabel('Days after 500 cases', fontsize=18)
    plt.title('Active Cases', fontsize=22, color='white')
    
    #Colors
    ax.set_facecolor('xkcd:black')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')


def get_rank():
    rank = build_df(file)
    rank = rank.sort_values('Confirmed')

    fig, ax = plt.subplots(1, figsize=(14,8), facecolor='black')

    myrange = 15
    countries = rank['Country'][-myrange:].values.tolist()

    color1 = 'orangered'
    color2 = 'grey'
    color3 = 'lightblue'

    for i, name in enumerate(countries):

        temp = rank[rank['Country'] == name]

        plt.plot([-temp['Deaths'].values[0], -temp['Recovered'].values[0]], [i, i], 
                 marker='o', color=color3, linewidth=4)

        plt.plot([0, -temp['Deaths'].values[0]], [i, i], 
                 marker='o', color=color2, linewidth=4)

        plt.plot([0, temp['Active'].values[0]], [i, i], 
                 marker='o', color=color1, linewidth=4)

    xticks = np.arange(-100000, 800001, 50000)
    xticks_label =[]

    for i in xticks:
        val = str(i)[:-3] + 'k'
        if i < 0:
            val = val[1:]
        elif i == 0:
            val = '|'

        xticks_label.append(val)

    plt.xticks(xticks, labels = xticks_label, fontsize=14)    

    # grid
    ax.grid(color='grey', linestyle='dashed', linewidth=1, axis = 'x')
    ax.set_axisbelow(True)

    # remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    #Colors, labels, ticks
    ax.set_facecolor('xkcd:black')
    plt.yticks(np.arange(len(countries)), color='white', 
               labels = countries, fontsize=12)
    plt.xticks(color='white')

    plt.ylim(-1,myrange)
    plt.title(file[:10], color='white', fontsize=22)
    plt.legend(['Recovered', 'Deaths', 'Active'], loc='lower right')
    plt.savefig('img/rank.png', facecolor='black', edgecolor='none')
 


