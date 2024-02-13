import pandas as pd
import json
import xml.etree.ElementTree as ET
import yaml

CSV_Data = pd.read_csv("../01._Data_Files/me.csv")

Json_File = open("../01._Data_Files/me.json") 
Json_Data = json.load(Json_File)

tree = ET.parse("../01._Data_Files/me.xml")
root = tree.getroot()

first_name = root.find("FirstName").text
last_name = root.find("LastName").text
age = int(root.find("age").text)
education_areas = [area.text for area in root.findall("./Education/Area")]

with open("../01._Data_Files/me.yaml", "r") as file:
    me_data = yaml.safe_load(file)


with open("../01._Data_Files/me.txt", "r") as file:
    data = {}
    for line in file:
        line = line.strip()
        key, value = line.split(":")
        if key in data:
            if isinstance(data[key], list):
                data[key].append(value)
            else:
                data[key] = [data[key], value]
        else:
            data[key] = value
print(data)
print("Data from me.csv: \n", CSV_Data)

print("Data from me.json: \n",Json_Data)

print("Data from me.xml:")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Age:", age)
print("Education Areas:", education_areas)

print("Data from me.yaml:")
print("First Name:", me_data["FirstName"])
print("Last Name:", me_data["LastName"])
print("Age:", me_data["Age"])
print("Education:", me_data["Education"])