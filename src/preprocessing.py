import pandas as pd
import numpy as np
import re


df=pd.read_csv("data/tickets.csv")
print(df)

print(df.isnull().sum())

print("Total duplicate rows:",df.duplicated().sum())

df=df.drop_duplicates()

def clean_text(text):
    text=text.lower()
    text=re.sub(r"[^a-z\s]"," ",text)
    text=re.sub(r"\s+"," ",text)
    text=text.strip()

    return text

df["ticket_description"]=df["ticket_description"].apply(clean_text)

print(df["ticket_description"].head(10))

print(df.info())
print("Total records:", len(df))
print("Rows and Columns:", df.shape)
print(df.describe(include="all"))

df.to_csv("data/cleaned_tickets.csv", index=False)