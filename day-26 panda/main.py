import pandas as pd

data = pd.read_csv("4.2 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = 0
cinnamon = 0
black = 0

for i in data["Primary Fur Color"].tolist():
    if i == "Gray":
        gray += 1
    elif i == "Cinnamon":
        cinnamon += 1
    elif i == "Black":
        black += 1
print(gray)
print(cinnamon)
print(black)