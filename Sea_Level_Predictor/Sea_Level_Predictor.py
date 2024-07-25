import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    """ Use Pandas to import the data from epa-sea-level.csv."""
    df = pd.read_csv("/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv")

    # Create scatter plot
    """ Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level 
        column as the y-axis."""
    fig, ax = plt.subplots(figsize=(20,10))
    # plot
    ax.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    """
    Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. 
    Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to 
    predict the sea level rise in 2050.
    """
    slope_intercept1 = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])

    df2 = pd.DataFrame()
    df2['Year'] = np.arange(1880,2051,1)
    df2['best_fit_line1_values'] = slope_intercept1.slope * df2['Year'] + slope_intercept1.intercept
    # plot
    ax.plot(df2['Year'],df2['best_fit_line1_values'],color ='red')
    

    # Create second line of best fit
    """
    Plot a new line of best fit just using the data from year 2000 through the most recent
    year in the dataset. Make the line also go through the year 2050 to predict the sea
    level rise in 2050 if the rate of rise continues as it has since the year 2000.
    """
    df3 = df[df['Year']>=2000]
    slope_intercept2 = linregress(df3['Year'],df3['CSIRO Adjusted Sea Level'])

    df4 = pd.DataFrame()
    df4['Year'] = np.arange(2000,2051,1)
    df4['best_fit_line2_values'] = slope_intercept2.slope * df4['Year'] + slope_intercept2.intercept
    # plot
    ax.plot(df4['Year'],df4['best_fit_line2_values'],color='green')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    plt.show()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
