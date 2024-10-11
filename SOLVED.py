import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    mx=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])[0]
    b=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])[1]
    ax.plot(np.arange(1880,2051),mx*np.arange(1880,2051)+b)


    # Create second line of best fit
    df1=df.loc[df['Year']>=2000]
    linregress(df1['Year'],df1['CSIRO Adjusted Sea Level'])
    mx1=linregress(df1['Year'],df1['CSIRO Adjusted Sea Level'])[0]
    b1=linregress(df1['Year'],df1['CSIRO Adjusted Sea Level'])[1]
    ax.plot(np.arange(2000,2051),np.arange(2000,2051)*mx1+b1)


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()