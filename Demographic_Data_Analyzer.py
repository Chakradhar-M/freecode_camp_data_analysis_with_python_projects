# Demographic Data Analyzer

import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("/workspace/boilerplate-demographic-data-analyzer/adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    ###################################################################################################################

    # What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(),1)

    ###################################################################################################################

    # What is the percentage of people who have a Bachelor's degree?
    workers_with_bachelors_degree = df[df["education"] == "Bachelors"]

    percentage_bachelors = round(((len(workers_with_bachelors_degree))/len(df))*100,1)

    ###################################################################################################################

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df["education"].isin(["Bachelors","Masters","Doctorate"])]
    higher_education_50Kabove = higher_education[higher_education["salary"] == ">50K"]

    lower_education = df[~(df["education"].isin(["Bachelors","Masters","Doctorate"]))]
    lower_education_50Kabove = lower_education[lower_education["salary"] == ">50K"]

    higher_education_rich = round(((len(higher_education_50Kabove))/(len(higher_education)))*100,1)

    lower_education_rich = round(((len(lower_education_50Kabove))/(len(lower_education)))*100,1)

    ###################################################################################################################

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_work_hours = df["hours-per-week"].min()
    
    min_hour_workers = df[df['hours-per-week'] == min_work_hours]

    rich_min_hour_workers = min_hour_workers[min_hour_workers["salary"] == ">50K"]

    rich_percentage = round((len(rich_min_hour_workers)/len(min_hour_workers))*100,4)
   
    ###################################################################################################################
    # Total number of individuals from each country
    total_workers_country_wise = df["native-country"].value_counts()

    # Filter high earners
    high_earners = df[df["salary"] == ">50K"]

    # Number of high earners from each country
    high_earners_country_wise = high_earners["native-country"].value_counts()

    # Calculate the percentage of high earners for each country
    percentage_high_earners_country_wise = (high_earners_country_wise / total_workers_country_wise) * 100

    # Find the country with the highest percentage of high earners
    highest_earning_country = percentage_high_earners_country_wise.idxmax()

    # Find the highest percentage
    highest_earning_country_percentage = round(percentage_high_earners_country_wise.max(),1)

    ###################################################################################################################  
    #     
    # Identify the most popular occupation for those who earn >50K in India.
    india_50k = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    top_IN_occupation = india_50k["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }