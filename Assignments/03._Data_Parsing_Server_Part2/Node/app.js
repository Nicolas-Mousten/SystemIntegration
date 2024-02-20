const express = require('express');
const path = require('path');
const fileParser = require("../../01._Program_Files/NodeParser")


const app = express()


app.get("/txtParser", (req, res) => {
    fileParser.readText("./Data_Files/me.txt", (err, data) => {
        console.log(data)
        res.send({ "data" : data });
    });
});

app.get("/csvParser", (req, res) => {
    fileParser.readCSV("./Data_Files/me.csv", (err, data) => {
        console.log(data)
        res.send({ "data" : data });
    });
});

app.get("/jsonParser", (req, res) => {
    fileParser.readJSON("./Data_Files/me.json", (err, data) => {
        console.log(data)
        res.send({ "data" : data });
    });
});

app.get("/xmlParser", (req, res) => {
    fileParser.readXML("./Data_Files/me.xml", (err, data) => {
        console.log(data)
        res.send({ "data" : data });
    });
});

app.get("/yamlParser", (req, res) => {
    fileParser.readYAML("./Data_Files/me.yaml", (err, data) => {
        console.log(data)
        res.send({ "data" : data });
    });
});
// ------------------------------------------------------------------------

app.get("/txtFastAPI", async (req, res) => {

    const response = await fetch("http://127.0.0.1:8000/txtParser");

    if (response.ok) {
        const responseData = await response.json();

        res.send({ responseData });
    }
});

app.get("/csvFastAPI", async (req, res) => {

    const response = await fetch("http://127.0.0.1:8000/csvParser");

    if (response.ok) {
        const responseData = await response.json();

        res.send({ responseData });
    }
});

app.get("/jsonFastAPI", async (req, res) => {

    const response = await fetch("http://127.0.0.1:8000/jsonParser");

    if (response.ok) {
        const responseData = await response.json();

        res.send({ responseData });
    }
});

app.get("/xmlFastAPI", async (req, res) => {

    const response = await fetch("http://127.0.0.1:8000/xmlParser");

    if (response.ok) {
        const responseData = await response.json();

        res.send({ responseData });
    }
});

app.get("/yamlFastAPI", async (req, res) => {

    const response = await fetch("http://127.0.0.1:8000/yamlParser");

    if (response.ok) {
        const responseData = await response.json();

        res.send({ responseData });
    }
});

const PORT = 8080;
app.listen(PORT, () => console.log("Server is running on port:", PORT));
