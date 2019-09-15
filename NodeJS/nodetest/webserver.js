var http = require('http').createServer(handler); // require http server, and create server with function handler()
var fs = require('fs'); // require filesystem module

http.listen(8040); // listn to port 8080

function handler (req, res) { // create server
  fs.readFile(_dirname + '/public/index.html', function(err, data) { // read file index.html in public folerr
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'}); // display 404 on error
      return res.end("404 Not Found");
    }
    res.writeHead(200, {'Content-type': 'text/html'}); // write HTML
    res.write(data); // write data from index.html
    return res.end();
  });
}

