import pandas as pd 
nov_df = pd.read_csv('November Feedback.csv',encoding='latin-1')
nov_df['Location'] = pd.Categorical(nov_df['Location'], ordered=True, 
                                   categories=['UK (Remote)','USA (Remote)', 'London (Remote)', 
                                              'Cardiff (Remote)'])

print(nov_df['Location'])
                     
