# import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# title placed here to consolidate length
title = 'Daily Mean PM2.5 Readings by EPA Monitoring Station:\n\
Louisville, KY area before and after the 3/3/23 windstorm.\n\
(PM2.5: lower reading = better air quality)' 

# read EPA data into DataFrame using only Date, Daily Mean PM2.5 Concentration, and Site Name columns
df = pd.read_csv('assets/EPA_PM2.5_DATA_LOUISVILLE_1-1-23_3-6-23.csv',
                 usecols=[0,4,7])

# create dataframe of only Jeffersonville station from 02/28 to 03/05
df_Jeffersonville = (df.loc[((df['Date'] >= '02/28/2023') & 
        (df['Site Name'] == 'Jeffersonville- Bates-Bowyer Ave.'))])
# create dataframe of only Watson Lane station from 02/28 to 03/05
df_Watson = (df.loc[((df['Date'] >= '02/28/2023') & 
        (df['Site Name'] == 'Watson Lane'))])
# create dataframe of only Cannons Lane station from 02/28 to 03/05
df_Cannons = (df.loc[((df['Date'] >= '02/28/2023') & 
        (df['Site Name'] == 'CANNONS LANE'))])
# create dataframe of only Durrett Lane station from 02/28 to 03/05
df_Durrett = (df.loc[((df['Date'] >= '02/28/2023') & 
        (df['Site Name'] == 'Durrett Lane (Near Road)'))])
# create dataframe of only Carrithers Middle School station from 02/28 to 03/05
df_Carrithers = (df.loc[((df['Date'] >= '02/28/2023') & 
        (df['Site Name'] == 'Carrithers Middle School'))])

# plot air quality data from created dataframes, on the same plot
airQ_plot = df_Jeffersonville.plot(x='Date', y='Daily Mean PM2.5 Concentration',
             title=title,
             ylabel='PM2.5',
             color='orange',
             label = 'Jeffersonville')
df_Watson.plot(x='Date', ax=airQ_plot, y='Daily Mean PM2.5 Concentration',
             color= 'blue',
             label = 'Watson Lane')
df_Cannons.plot(x='Date', ax=airQ_plot, y='Daily Mean PM2.5 Concentration',
             color= 'green',
             label = 'Cannons Lane')
df_Durrett.plot(x='Date', ax=airQ_plot, y='Daily Mean PM2.5 Concentration',
             color= 'purple',
             label = 'Durrett Lane')
df_Carrithers.plot(x='Date', ax=airQ_plot, y='Daily Mean PM2.5 Concentration',
             color='red',
             label= 'Carrithers Middle School')

# adjust legend
plt.legend(labelspacing=0.0125)
# show plotted data
plt.show()
