# Data From https://www.kaggle.com/imdevskp/corona-virus-report
import numpy as np
import pandas as pd 
import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import moviepy.editor as mp
from IPython.display import Video

from methods import plot_rank, plot_day, plot_map, build_gif

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world[~world.name.isin(["Antarctica", "Fr. S. Antarctic Lands"])]
#PATH = "C:/py/covid19/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
path = 'data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/'

file = '05-10-2020.csv'
today = '05-10-2020'
today = pd.to_datetime(today, format = "%m-%d-%Y")
df = pd.read_csv(path+file)
df.head()



### MAPS ###
print('printing maps')
# create file name range from 03-01-2020 **First update with lat and long
dates = pd.date_range(start="03-01-2020",end=today)
files = []

# create a list of datasets filenames
for i in dates.strftime('%m-%d-%Y'):
    files.append(str(i)+'.csv')
    
# create maps
for file in files:
    plot_map(pd.read_csv(path+file), file[:10])
    plt.close('all')
    if(files[-1] == file): print('Concluded')
        
# Build files list
break_size = int( len( files) / 4)
clip_list = []

# use break size to define how many times to repeat the images in each break.
# This gives us some control on how fast the imgs transition in each part of the video/.gif
for i, file in enumerate(files):
    
    filename = 'img/video/'+file[:10]+'_map.png'
    
    if(i == len(files)-1):
        clip_list.extend([filename for i in range(15)])
    elif(i > break_size*3):
        clip_list.extend([filename for i in range(3)])
    elif(i > break_size*2):
        clip_list.extend([filename for i in range(2)])
    else:
        clip_list.append(filename)

# build map video       
clip = mp.ImageSequenceClip(clip_list, fps=3)
clip.write_videofile("img/map_timeseries.mp4")

# build gif
build_gif(clip_list, 'img/map_timeseries', duration=0.3)



### RANKS ###
print('printing ranks')
# create a list of datasets filenames
files = []
for i in dates.strftime('%m-%d-%Y'):
    files.append(str(i)+'.csv')

# create maps
for file in files:
    plot_day(pd.read_csv(path+file), file[:10])
    plt.close('all')

# Build files list
break_size = int( len( files) / 4)
clip_list = []

# use break size to define how many times to repeat the images in each break.
# This gives us some control on how fast the imgs transition in each part of the video/.gif
for i, file in enumerate(files):
    filename = 'img/video/'+file[:10]+'.png'
    # define
    if(i == len(files)-1):
        clip_list.extend([filename for i in range(15)])
    elif(i > break_size*3):
        clip_list.extend([filename for i in range(3)])
    elif(i > break_size*2):
        clip_list.extend([filename for i in range(2)])
    else:
        clip_list.append(filename)

# build map video  
clip = mp.ImageSequenceClip(clip_list, fps=2)
clip.write_videofile("img/rank_timeseries.mp4")

# build gif
build_gif(clip_list, 'img/rank_timeseries', duration=0.3)