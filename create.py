import pandas as pd
from dataclasses import dataclass 
from jinja2 import Environment, FileSystemLoader
from typing import List

@dataclass 
class Line: 
    speaker: str 
    de: List[str]
    en: List[str]

    def str(self) -> str: 
        return f"Speaker: {self.speaker}, de: {self.de}, en: {self.en}"

lines = []
counter = 0
# with open('inp.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     for row in spamreader:
#         print(counter, ": ", row)
#         speaker = row[0] 
#         de = row[1] 
#         en = row[2] if len(row) > 2 else f"missing translation: {de}"
# 
#         lines.append(Line(speaker, de, en))
#         counter += 1

df = pd.read_excel(r"inp.xlsx", header=None)
print(df)

for index, row in df.iterrows():
    speaker = row[0]
    de = str(row[1])
    en = str(row[2])

    list_de = de.split("\n")
    list_en = en.split("\n")
    lines.append(Line(speaker, list_de, list_en))

for i in range(10): 
    print(lines[i].str())

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.tex')

# Define the data to be rendered
data = {"lines": lines}

# Render the template with the data
output = template.render(data)

# Save the rendered output to a file
with open('main.tex', 'w') as f:
    f.write(output)
