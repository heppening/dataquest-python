import csv
import datetime

f = open("guns.csv", 'r')
data = list(csv.reader(f))

headers = data[0]
data = data[1:]

years = [row[1] for row in data]
year_counts = {}
for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1

dates = [datetime.datetime(int(row[1]), int(row[2]), 1) for row in data]
date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1

sex = [row[5] for row in data]
sex_counts = {}
for s in sex:
    if s in sex_counts:
        sex_counts[s] += 1
    else:
        sex_counts[s] = 1

race1 = [row[7] for row in data]
race_counts  = {}
for r in race1:
    if r in race_counts:
        race_counts [r] += 1
    else:
        race_counts [r] = 1

f1 = open("census.csv", 'r')
census = list(csv.reader(f1))
mapping = {
    "Asian/Pacific Islander": 15159516 + 674625,
    "Black": 40250635,
    "White": 197318956,
    "Native American/Native Alaskan": 3739506,
    "Hispanic": 44618105
}

race_per_hundredk = {}
for k,v in race_counts.items():
    race_per_hundredk[k] = (v / mapping[k]) * 100000

intents = [row[3] for row in data]
races = [row[7] for row in data]
homicide_race_counts = {}

for i, race in enumerate(races):
    if intents[i] == "Homicide":
        if race in homicide_race_counts:
            homicide_race_counts [race] += 1
        else:
            homicide_race_counts [race] = 1
            
homeciderace_per_hundredk = {}
for k,v in homicide_race_counts.items():
    homeciderace_per_hundredk[k] = (v / mapping[k]) * 100000

print(homeciderace_per_hundredk)
