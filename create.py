from numpy import append
import pandas as pd
from dataclasses import dataclass 
from jinja2 import Environment, FileSystemLoader
from typing import List

@dataclass 
class Line: 
    speaker: str 
    de: List[str]
    en: List[str]
    index: int

    def str(self) -> str: 
        return f"Speaker: {self.speaker}, de: {self.de}, en: {self.en}"


df = pd.read_excel(r"inp.xlsx", header=None)
print(df)

lines = []
for index, row in df.iterrows():
    speaker = str(row[0])
    de = str(row[1])
    en = str(row[2])
    line_num = (index)+1

    list_de = de.split("\n")
    list_en = en.split("\n")

    if list_de[0] != "nan" or list_en[0] != "nan":
        lines.append(Line(speaker, list_de, list_en, line_num))
    else: 
        lines[-1].de.append("SZENEN ENDE!")

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
