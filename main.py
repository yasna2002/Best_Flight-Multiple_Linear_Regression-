import pandas as pd

df = pd.read_csv("Flight_Data.csv")
data2 = df.drop(columns='Airline')
df2 = data2.drop_duplicates(keep='first')
extracted_col = df["Airline"]
df2.insert(0, 'Airline', extracted_col)


user_input = input("Please enter source and destination airport:")
input_split = user_input.split(" - ")
src_port = input_split[0]  # putting input airports in variables
dest_port = input_split[1]
