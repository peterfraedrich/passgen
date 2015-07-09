// PASSGEN
//
//

// SETUP ==============================================================//
 var connect = require('connect');
    var sys = require('sys');
    var exec = require('child_process').exec;
    var fs = require ('fs');
    var zerorpc = require ('zerorpc');
    var application_root = __dirname,
        express = require('express'),
        bodyParser = require('body-parser'),
        methodOverride = require('method-override'),
        errorhandler = require('errorhandler'),
            path = require('path');
        var app = express();
  
    var httpPort = 80;
    var apiPort = 8080;

// CONFIG ==============================================================//

var allowCrossDomain = function(req, res, next) {
      res.header('Access-Control-Allow-Origin', '*');
      //res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
      res.header('Access-Control-Allow-Methods', '*');
      res.header('Access-Control-Allow-Headers', '*');
      //res.header('Access-Control-Allow-Headers', 'X-Requested-With, Accept, Origin, Referer, User-Agent, Content-Type, Authorization');
     
      // intercept OPTIONS method
      if (req.method === 'OPTIONS') {
        res.send(200);
      }
      else {
        next();
      }
    };

    app.use(allowCrossDomain);   // make sure this is is called before the router
    app.use(bodyParser());
    app.use(methodOverride());
    app.use(errorhandler());
    app.use(express.static(path.join(application_root, "public")));

// INTERNAL FUNCTIONS ====================================================//

// SET UP RPC ============================================================//

  var client = new zerorpc.Client();
  function rpc() {
  	client.connect('tcp://127.0.0.1:8081');
  	var password = client.invoke('generate','RPC', function(error, res, more) {
  		  return res;
      });
    return password;
  };

// API HOOKS ==============================================================//

//// TEST HOOK
	app.get('/api', function (req, res) {
		res.send('API OK');
		res.end();
	});

//// GENERATE
	app.get('/generate', function (req, res) {
		client.connect('tcp://127.0.0.1:8081');
		client.invoke('generate','RPC', function(error, res, more) { global.password = res; })
		res.send(global.password);	
		res.end();
	});


// SERVER ==================================================================//

connect ()
  .use(connect.static(__dirname)).listen(httpPort);
console.log('Web server listening on port 80');
app.listen(apiPort);
console.log('API listening on port 8080');
