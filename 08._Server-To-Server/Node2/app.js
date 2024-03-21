import express from "express";

const app = express();

app.get('/date', (req, res) => {
    const currentDate = new Date();
    res.send(currentDate);
  });


const PORT = 8080;
app.listen(PORT, () => console.log("Server is running on port:", PORT));
