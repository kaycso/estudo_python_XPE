const http = require("http");
const fs = require("fs").promises;

const host = "localhost";
const port = 8000;

const loadHtmlFile = (fileName, res) => {
    fs.readFile(__dirname + fileName).then((contents) => {
        res.setHeader("Content-Type", "text/html")
        res.writeHead(200);
        res.end(contents)
    });
};

const server = http.createServer(function (req, res) {
    switch (req.url) {
        case "/":
            loadHtmlFile("/index.html", res);
            break;
        case "/autor":
            loadHtmlFile("/autor.html", res);
            break;
        case "/livro":
            loadHtmlFile("/livro.html", res);
            break;
        default:
            res.writeHead(404);
            res.end(JSON.stringify({ error: "Resource Not Found" }))
    }
});

server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});