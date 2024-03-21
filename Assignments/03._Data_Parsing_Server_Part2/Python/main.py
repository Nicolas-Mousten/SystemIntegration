from fastapi import FastAPI;
import requests
import sys
sys.path.append(r'C:\Users\udh12\Desktop\SystemIntegration\Assignments\01._Program_Files')
import PythonParser


app = FastAPI()

@app.get("/txtParser")
def _():
    text_data = PythonParser.parse_text("Data_Files/me.txt")
    return text_data

@app.get("/csvParser")
def _():
    CSV_Data = PythonParser.read_csv("Data_Files/me.csv")
    return CSV_Data

@app.get("/jsonParser")
def _():
    Json_Data = PythonParser.read_json("Data_Files/me.json")
    return Json_Data

@app.get("/xmlParser")
def _():
    Xml_Data = PythonParser.parse_xml("Data_Files/me.xml")
    return Xml_Data

@app.get("/yamlParser")
def _():
    me_data = PythonParser.read_yaml("Data_Files/me.yaml")
    return me_data
#------------------------------------------------------------------------

@app.get("/txtExpress")
def _():

    url = "http://127.0.0.1:8080/txtParser"

    response = requests.get(url).json()

    return { "data" : response } 

@app.get("/csvExpress")
def _():

    url = "http://127.0.0.1:8080/csvParser"

    response = requests.get(url).json()

    return { "data" : response } 

@app.get("/jsonExpress")
def _():

    url = "http://127.0.0.1:8080/jsonParser"

    response = requests.get(url).json()

    return { "data" : response } 

@app.get("/xmlExpress")
def _():

    url = "http://127.0.0.1:8080/xmlParser"

    response = requests.get(url).json()

    return { "data" : response } 

@app.get("/yamlExpress")
def _():

    url = "http://127.0.0.1:8080/yamlParser"

    response = requests.get(url).json()

    return { "data" : response } 