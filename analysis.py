import pandas as pd
df=pd.read_csv("api_data_aadhar_enrolment_0_500000.csv")
print(df.head())
print(df["state"].unique())