import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('/workspace/boilerplate-page-view-time-series-visualizer/fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
#print(df.shape)

# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[(df['value']>=df['value'].quantile(0.025)) & (df['value']<=df['value'].quantile(0.975))]
#print(df.shape)

def draw_line_plot():
    # Draw line plot
    """ Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". 
    The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date 
    and the label on the y axis should be Page Views """

    df_line = df.copy()

    fig,ax = plt.subplots(1,1,figsize=(25,8))
    ax.plot(df_line.index,df_line['value'],color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    #plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    """
    Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". 
    It should show average daily page views for each month grouped by year. The legend should 
    show month labels and have a title of Months. On the chart, the label on the x axis should 
    be Years and the label on the y axis should be Average Page Views.
    """
    # Copy and modify data for monthly bar plot   
    df_bar = df.copy()
    df['year'] = df.index.year
    df['month'] = df.index.month_name()
    df_bar = df.groupby(['year', 'month'])['value'].mean().reset_index()
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=[
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ], ordered=True)
    df_bar = df_bar.sort_values(['year', 'month'])

    # Draw bar plot using Matplotlib
    fig, ax = plt.subplots(figsize=(15, 12))

    # Pivot data for easy plotting
    df_pivot = df_bar.pivot(index='year', columns='month', values='value')
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']

    # Define the bar width and positions
    bar_width = 0.5
    bar_positions = np.arange(len(df_pivot.index))

    # Plot bars for each month
    for i, month in enumerate(month_order):
        values = df_pivot[month].values
        ax.bar(bar_positions + i * bar_width / len(month_order), values, bar_width / len(month_order), label=month)

    # Customize the plot
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months',loc='upper left')
    ax.set_xticks(bar_positions + bar_width / 2)
    ax.set_xticklabels(df_pivot.index)
    ax.tick_params(axis='x', rotation=90)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    """
    Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to 
    "examples/Figure_3.png". These box plots should show how the values are distributed within a 
    given year or month and how it compares over time. The title of the first chart should be 
    Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). 
    Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. 
    The boilerplate includes commands to prepare the data.
    """

    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month
    df_box['month_name'] = df_box['month'].apply(lambda x:pd.to_datetime(x, format='%m').strftime('%b'))

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(25,10))
    sns.boxplot(data=df_box, x= 'year', y='value', ax=ax[0], hue='year',legend=False)
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    sns.boxplot(data=df_box, x='month_name', y='value', ax=ax[1], order=month_order, hue='month_name',legend=False)
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    #plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

