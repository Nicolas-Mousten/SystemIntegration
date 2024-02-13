from flask import Flask
app = Flask(__name__)
import pandas as pd
import json
import xml.etree.ElementTree as ET
import yaml


@app.route("/txt")
def txtAPI():
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
    return data
@app.route("/json")
def jsonApi():
    Json_File = open("../01._Data_Files/me.json") 
    Json_Data = json.load(Json_File)
    return Json_Data

@app.route("/xml")
def xmlApi():
    tree = ET.parse("../01._Data_Files/me.xml")
    root = tree.getroot()
    first_name = root.find("FirstName").text
    last_name = root.find("LastName").text
    age = int(root.find("age").text)
    education_areas = [area.text for area in root.findall("./Education/Area")]
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "education_areas": education_areas
    }

@app.route("/yaml")
def yamlApi():
    with open("../01._Data_Files/me.yaml", "r") as file:
        me_data = yaml.safe_load(file)
    return me_data
@app.route("/csv")
def csvApi():
    CSV_Data = pd.read_csv("../01._Data_Files/me.csv")
    return CSV_Data
if __name__ == "__main__":
    app.run(debug=True)