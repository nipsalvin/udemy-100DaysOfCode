import pandas as pd

df=pd.read_csv('salaries_by_college_major.csv')
df.head() #Shows first `n` rows. Default is 5
df.shape #Returns layout of the dataframe (rows, comulmns)
df.columns #Returns column labels
df.isna() #Detect missing values and returns Boolean
df.tail() #Returns last `n` rows. Default is 5

clean_df = df.dropna() #Creates clean_df having dropped all rows that have NaN values
clean_df.tail() #Returns last `n` rows. Default is 5

clean_df['Starting Median Salary'] #Returns values from column with that label
clean_df['Starting Median Salary'].max() #Returns maximum value from that column
clean_df['Starting Median Salary'].idxmax() #Returns ID off column with MAX value
clean_df['Undergraduate Major'].loc[43] #Returns the `Undergraduate Major` that corresponds with `row_id 43`
clean_df['Undergraduate Major'][43] #Method 2
clean_df.loc[43] #Returns row at id 43 if a specific column in not specified

highest_starting_salary_id = clean_df['Mid-Career Median Salary'].idxmax()
highest_starting_salary_major =  clean_df['Undergraduate Major'].loc[highest_starting_salary_id]
earning_with_highest_mid_carrer = clean_df['Mid-Career Median Salary'].max()

lowest_starting_salary_id = clean_df['Starting Median Salary'].idxmin()
lowest_starting_salary_major = clean_df['Undergraduate Major'].loc[lowest_starting_salary_id]
people_earning_lowest_starting_salary = clean_df['Mid-Career 90th Percentile Salary'].loc[lowest_starting_salary_id]
people_expect_to_earn_with_this_major  = clean_df['Mid-Career Median Salary'].loc[lowest_starting_salary_id]
