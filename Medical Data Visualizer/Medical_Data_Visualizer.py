import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Import the data from medical_examination.csv and assign it to the df variable
df = pd.read_csv("/workspace/boilerplate-medical-data-visualizer/medical_examination.csv")
#print(df.head())

# 2 Create the overweight column in the df variable
df['BMI'] = (df["weight"]/((df["height"])*0.01)**2)
df['overweight'] = df['BMI'].apply(lambda x: 1 if x>25 else 0) # 1 overweight, 0 not overweight

# 3 Normalize data by making 0 always good and 1 always bad. 
# If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x==1 else 1) # 0 good, 1 bad
df['gluc'] = df['gluc'].apply(lambda x: 0 if x==1 else 1) # 0 good, 1 bad

# 4 Draw the Categorical Plot in the draw_cat_plot function
def draw_cat_plot():

    # 5 Create a DataFrame for the cat plot using pd.melt with values from 
    # cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    df_cat = pd.melt(df, id_vars=['id','cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'], var_name = "variable", value_name = "binary")
    

    # 6 Group and reformat the data in df_cat to split it by cardio. 
    # Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'binary']).size().reset_index(name='total')

    # 7 catplot using seaborn
    sns.catplot(x='variable', y='total', hue='binary', col='cardio', data=df_cat, kind='bar')

    # 8 Get the figure for the output and store it in the fig variable
    fig = plt.gcf()

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():

    # 11 Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    df_heat = df_heat.drop(columns=['BMI'])
    # 12 Create a correlation matrix
    corr = df_heat.corr()
    
    # 13 Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # 14 Set up the matplotlib figure
    plt.figure(figsize=(10, 8))
    
    # 15 Plot the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', center=0, square=True, linewidths=.5)
    
    # 16
    fig = plt.gcf()
    fig.savefig('heatmap.png')
    return fig


