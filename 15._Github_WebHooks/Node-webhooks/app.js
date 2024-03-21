import express from "express";

const app = express();

app.use(express.json()); //allows parse json
app.use(express.urlencoded({extended: true})); //allows parse url encoded forms


app.post("/githubWebhookjson", (req, res) =>{
    console.log(req.body);
    res.sendStatus(204);
});

app.post("githubwebhookform", (req,res) => {
    console.log(req.body);
    res.sendStatus(204);
});

app.listen(8080, () => console.log("Server is running on port", 8080));