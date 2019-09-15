// load the http module to create an http server
var http = require('http');

// Configure our HTTP server to respond with Hello World to all requests
var server = http.createServer(function (request, response) {
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.end("Hello World!\n");
});

// listen on port 8080, Ip defaults to 127.0.0.1
server.listen(8080);

// Put a friendly message on the terminal
console.log("Server running at http://127.0.0.1:8080\n");

