import pandas as pd
import os

#create a sample dataframe
data= {'Name': ['alice','bob','cats'],
       'Age':[25,46,34],
       'City':['LA','NY','CAL']}
df = pd.DataFrame(data)

#new row
new_row_loc = {'Name':'sem','Age': 24,'City':'lon'}
df.loc[len(df.index)] = new_row_loc

#ensure that "data" directory exists at root level
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

#define the file path
file_path= os.path.join(data_dir,'sample_data.csv')

#save data frame to csv file
df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")