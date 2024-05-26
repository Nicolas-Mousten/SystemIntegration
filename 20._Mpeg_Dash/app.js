import express from "express";
const app = express();

app.use(express.static("Public"));
app.use(express.static("videos"));

const PORT = process.env.PORT ?? 8080;
app.listen(PORT, () => console.log("Server os Running on port:", PORT))