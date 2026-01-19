import pandas as pd
# df=pd.read_csv("api_data_aadhar_enrolment_0_500000.csv")
# print(df.head())
# print(df["state"].unique())
files=["api_data_aadhar_enrolment_0_500000.csv","api_data_aadhar_enrolment_500000_1000000.csv","api_data_aadhar_enrolment_1000000_1006029.csv"]
df=pd.concat([pd.read_csv(f) for f in files],ignore_index=True)
print("Total Records:",len(df))
print("Unique Raw States:",df['state'].nunique())
# print("Unique Raw States:",df['state'].unique())
df["state_clean"]=df['state'].str.lower().str.strip()
print(sorted(df["state_clean"].unique()))
print("Unique Raw States:",df['state_clean'].nunique())

fix_map = {
    "orissa": "odisha",
    "pondicherry": "puducherry",

    "west bangal": "west bengal",
    "westbengal": "west bengal",
    "west  bengal": "west bengal",

    "jammu & kashmir": "jammu and kashmir",

    "andaman & nicobar islands": "andaman and nicobar islands",

    "dadra & nagar haveli": "dadra and nagar haveli and daman and diu",
    "daman and diu": "dadra and nagar haveli and daman and diu",
    "daman & diu": "dadra and nagar haveli and daman and diu",
    "dadra and nagar haveli": "dadra and nagar haveli and daman and diu",
    "the dadra and nagar haveli and daman and diu":"dadra and nagar haveli and daman and diu",

    "100000": None
}
df["state_clean"] =df["state_clean"].replace(fix_map)
df=df[df['state_clean'].notna()]

print(df["state_clean"].nunique())
print(sorted(df["state_clean"].unique()))