import pandas as pd 

sep_df = pd.read_csv('September Feedback.csv',encoding='latin-1')
columns_to_delete = ['Applied On', 'Collected On', 'Anonymized Contact ID', 'Posting ID',
                   'Current Stage ID','Application Archive Reason', 'Application Archived On',
       'Application Archived By', 'Survey Id', 'Survey Name',
       'Survey Location Type','Candidate Selected Location',
       'Stage - New lead', 'Stage - Reached out', 'Stage - Responded',
       'Stage - New applicant', 'Stage - Under review',
       'Stage - Recruiter Screen', 'Stage - Hiring Manager Screen',
       'Stage - 1st Round', 'Stage - 2nd Round', 'Stage - Decision',
       'Stage - Offer','What suggestions would you make to improve our interview process? - 21866cc4-7d8f-47da-97df-9efdfcbe083d','Origin','Sources']
final_sep_df = sep_df.drop(columns_to_delete,axis=1) 
sep_df1 = final_sep_df.style.background_gradient(cmap='Oranges')
print(sep_df1.to_string)
