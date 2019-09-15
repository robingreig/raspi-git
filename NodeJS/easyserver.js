var http = require('http');
var server = http.createServer(function(req, res) {
  res.writeHead('I created this server!');
  res.end();
});
server.listen(8080);
