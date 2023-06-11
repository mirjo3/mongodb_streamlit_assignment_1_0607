import pandas as pd
import requests

class Base:
    def __init__(self):
        self.df = pd.read_csv(r'C:\Users\jmira\OneDrive\Coding Temple Cohort 0501 0623\github\mongodb_streamlit_assignment_1_0607\student-mat.csv', sep= ';')

        # Step 1 : Lower case all columns
        self.df.columns = self.df.columns.str.lower()

        # Step 2 : rename columns
        self.df.rename(columns={
        'famsize': 'fam_size',
        'p_status]': 'p_status',
        'medu': 'mother_education',
        'fedu': 'father_education',
        'mjob': 'mother_job',
        'fjob': 'father_job',
        'traveltime': 'travel_time',
        'studytime': 'study_time',
        'schoolsup': 'school_support',
        'famsup': 'family_support',
        'famrel': 'family_relationship',
        'goout': 'going_out',
        'dalc': 'workday_alcohol_consumption',
        'walc': 'weekend_alcohol_consumption'
        }, inplace=True)
        self.df = self.df.rename_axis('', axis='rows').rename_axis('student_id', axis='columns')

print('Renaming columns successful')
if __name__ == '__main__':
    c = Base()
    c.df.to_csv('student_performance.csv')
print('CSV successfully made')
