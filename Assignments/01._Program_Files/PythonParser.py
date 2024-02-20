import pandas as pd
import json
import xml.etree.ElementTree as ET
import yaml

def parse_text(file_path):
    data = {}
    with open(file_path, "r") as file:
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
    return data

def read_csv(file_path):
    data = pd.read_csv(file_path)
    return data.to_json(orient='columns')

def read_json(file_path):
    with open(file_path) as Json_File:
        return json.load(Json_File)

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    first_name = root.find("FirstName").text
    last_name = root.find("LastName").text
    age = int(root.find("age").text)
    education_areas = [area.text for area in root.findall("./Education/Area")]
    return {"FirstName":first_name, "LastName":last_name, "Age":age, "Education":education_areas}

def read_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

# # Read data
# CSV_Data = read_csv("../01._Data_Files/me.csv")
# Json_Data = read_json("../01._Data_Files/me.json")
# Xml_Data = parse_xml("../01._Data_Files/me.xml")
# me_data = read_yaml("../01._Data_Files/me.yaml")
# text_data = parse_text("../01._Data_Files/me.txt")

# # Display data
# print("Data from me.txt: \n", text_data)
# print("Data from me.csv: \n", CSV_Data)
# print("Data from me.json: \n", Json_Data)
# print("Data from me.xml: \n", Xml_Data)
# print("Data from me.yaml: \n", me_data)





