# import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# title placed here as string to consolidate length
title = 'Louisville Area EPA Air Quality Measurements by Weather Station\n \
(PM2.5: Lower reading = better air quality)\n\
March 3rd windstorm results in better air quality readings.' 

# set plot DPI higher to improve appearance
plt.rcParams["figure.dpi"] = 250

# read EPA data in
df = pd.read_csv('assets/EPA_PM2.5_DATA_LOUISVILLE_1-1-23_3-6-23.csv',
                 usecols=[0,4,7],
                 parse_dates=True)

# create dataframe of Jeffersonville station from 02/28 to 03/05
df_Jeffersonville = (df.loc[((df['Date'] >= '02/28/2023') & 
        (df['Site Name'] == 'Jeffersonville- Bates-Bowyer Ave.'))])
# create dataframe of Watson Lane station from 02/28 to 03/05
df_Watson = (df.loc[((df['Date'] >= '02/28/2023') & 
        (df['Site Name'] == 'Watson Lane'))])
# create dataframe of Cannons Lane station from 02/28 to 03/05
df_Cannons = (df.loc[((df['Date'] >= '02/28/2023') & 
        (df['Site Name'] == 'CANNONS LANE'))])
# create dataframe of Durrett Lane station from 02/28 to 03/05
df_Durrett = (df.loc[((df['Date'] >= '02/28/2023') & 
        (df['Site Name'] == 'Durrett Lane (Near Road)'))])
# create dataframe of Carrithers Middle School station from 02/28 to 03/05
df_Carrithers = (df.loc[((df['Date'] >= '02/28/2023') & 
        (df['Site Name'] == 'Carrithers Middle School'))])

# plot air quality data
airQ_plot = df_Jeffersonville.plot(x='Date', y='Daily Mean PM2.5 Concentration',
             title=title,
             ylabel='PM2.5',
             color='orange',
             label = 'Daily Mean PM2.5 Concentration: Jeffersonville')
df_Watson.plot(x='Date', ax=airQ_plot, y='Daily Mean PM2.5 Concentration',
             color= 'blue',
             label = 'Daily Mean PM2.5 Concentration: Watson Lane')
df_Cannons.plot(x='Date', ax=airQ_plot, y='Daily Mean PM2.5 Concentration',
             color= 'green',
             label = 'Daily Mean PM2.5 Concentration: Cannons Lane')
df_Durrett.plot(x='Date', ax=airQ_plot, y='Daily Mean PM2.5 Concentration',
             color= 'purple',
             label = 'Daily Mean PM2.5 Concentration: Durrett Lane')
df_Carrithers.plot(x='Date', ax=airQ_plot, y='Daily Mean PM2.5 Concentration',
             color='red',
             label= 'Daily Mean PM2.5 Concentration: Carrithers Middle School')

# place legend to the left of the plot
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
