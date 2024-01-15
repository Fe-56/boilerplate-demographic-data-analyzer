import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df['race'].value_counts()

  # What is the average age of men?
  df_men = df.loc[df['sex'] == 'Male']
  average_age_men = df_men['age'].mean().round(1)

  # What is the percentage of people who have a Bachelor's degree?
  df_bachelors = df.loc[df['education'] == 'Bachelors']
  num_bachelors = df_bachelors.shape[0]
  total_num_people = df.shape[0]
  percentage_bachelors = round(((num_bachelors / total_num_people) * 100), 1)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_education = ['Bachelors', 'Masters', 'Doctorate']
  df_higher_education = df.loc[df['education'].isin(higher_education)]
  df_lower_education = df.loc[~df['education'].isin(higher_education)]

  # percentage with salary >50K
  num_higher_education_rich = df_higher_education.loc[
      df_higher_education['salary'] == '>50K'].shape[0]
  total_num_higher_education = df_higher_education.shape[0]
  num_lower_education_rich = df_lower_education.loc[
      df_lower_education['salary'] == '>50K'].shape[0]
  total_num_lower_education = df_lower_education.shape[0]
  higher_education_rich = round(
      ((num_higher_education_rich / total_num_higher_education) * 100), 1)
  lower_education_rich = round(
      ((num_lower_education_rich / total_num_lower_education) * 100), 1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  df_min_workers = df.loc[df['hours-per-week'] == min_work_hours]
  num_min_workers = df_min_workers.shape[0]
  num_rich_min_workers = df_min_workers.loc[df_min_workers['salary'] ==
                                            '>50K'].shape[0]
  rich_percentage = round(((num_rich_min_workers / num_min_workers) * 100), 1)

  # What country has the highest percentage of people that earn >50K?
  country_percentage_rich = {}

  for index, df_country in df.groupby('native-country'):
    country = df_country.iloc[0]['native-country']
    num_rich_people_country = df_country.loc[df_country['salary'] ==
                                             '>50K'].shape[0]
    total_num_people_country = df_country.shape[0]
    percentage_rich_people_country = round(
        ((num_rich_people_country / total_num_people_country) * 100), 1)
    country_percentage_rich[country] = percentage_rich_people_country

  highest_earning_country = max(country_percentage_rich,
                                key=country_percentage_rich.get)
  highest_earning_country_percentage = country_percentage_rich[
      highest_earning_country]

  # Identify the most popular occupation for those who earn >50K in India.
  df_india = df.loc[df['native-country'] == 'India']
  df_india_rich = df_india.loc[df_india['salary'] == '>50K']
  top_IN_occupation = df_india_rich['occupation'].mode().values[0]

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
        f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
        f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
        f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
        f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
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
      'highest_earning_country_percentage': highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
  }
