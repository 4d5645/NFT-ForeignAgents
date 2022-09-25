import sys
import json
import pandas as pd
from datetime import date

  
with open(sys.argv[1]) as f:
    data = json.load(f)
macknack = []
for i in data["messages"]:
    dt = i["date"]
    year, month, day = int(dt[:4]), int(dt[5:7]), int(dt[8:10])
    dt = date(year, month, day)
    if dt > date(2022, 2, 24):
        macknack.append(i)
    else:
        continue

df = pd.DataFrame(macknack)
df.to_csv(sys.argv[2])
