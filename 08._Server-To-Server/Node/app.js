import express from "express";

const app = express();

app.get("/requestFastAPI", async (req, res) => {

    const response = await fetch("http://127.0.0.1:8000/fastapiData");

    if (response.ok) {
        const responseData = await response.json();

        res.send({ responseData });
    }
});

app.get("/expressData", (req, res) => {
    res.send({ "isRunning" : true });
});


const PORT = 8080;
app.listen(PORT, () => console.log("Server is running on port:", PORT));
