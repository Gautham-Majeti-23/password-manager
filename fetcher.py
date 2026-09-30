"""
Takes user input and then fetches the password to the corresponding service.
"""
import pandas as pd

# Initiate pandas dataframe from the storage CSV.
df = pd.read_csv("passwords.csv")

print(df["service"])

# Taking user input.
service = input("Enter Service name: ").lower()

# Finding index of the service.
index = 0

for i in df["service"]:
    if i.lower() == service:
        break
    else:
        index += 1

# Displays the corresponding password.
print(df.iat[index, 1])
1