import  express  from "express";
const app = express();

app.use(express.static("public"));

app.get("/synchronize-time", (req, res) =>{
    res.writeHead(200, { 
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive"
    });

    setInterval(() => sendTimeToClient(res), 1000);//scadelerar i event loopet
});

console.log(new Date().toISOString());

function sendTimeToClient(res){ //stand alone functions is ok as this but class functions should be arrow functions
    const time = new Date().toISOString();
    res.write(`data: ${time} \n\n`)//\n\n is syntac must
};

const PORT = 8080;
app.listen(PORT, () => console.log("Server is running on port:",PORT))