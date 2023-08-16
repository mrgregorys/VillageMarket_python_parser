import os
import yaml
from yaml.loader import SafeLoader
import json

path = 'logs/'
#json = "data.json"


sold_data = {}
bought_data = {}

for dir, folder, files in os.walk(path):
    for filename in files:
        with open(path + filename) as f:
            data = yaml.load(f, Loader=SafeLoader)
            for i in range (0, len(data["log"])):
                sold_data[data["log"][i].split()[9]] = 0
                bought_data[data["log"][i].split()[9]] = 0

for dir, folder, files in os.walk(path):
    for filename in files:
        with open(path + filename) as f:
            data = yaml.load(f, Loader=SafeLoader)
            for i in range(0, len(data["log"])):
                if data['log'][i].split()[7] == 'sold':
                    count = data["log"][i].split()[8]
                    count = int(count.strip("x"))
                    item = data["log"][i].split()[9]
                    sold_data[item] = sold_data[item] + count
                else:
                    count = data["log"][i].split()[8]
                    count = int(count.strip("x"))
                    item = data["log"][i].split()[9]
                    bought_data[item] = bought_data[item] + count


print("Sell data")
print(json.dumps(sold_data,indent=4))
print()
print("Bought data")
print(json.dumps(bought_data,indent=4))
