var express = require('express');
var app = express();
var childProc = require("child_process")


app.post('/deal-closed', function (req, res) {
  res.send('Dealguy is ON and in deal closed mode.');
  setTimeout(function(){
    var process = childProc.spawn('python',["/home/pi/dealguy/theguy.py", "closed"]);
    console.log('Deal guy is running in deal closed mode.');
    process.stdout.on('data', function (data){
      console.log(data.toString());
    });
  }, 1);
});

app.post('/deal-morale', function (req, res) {
  res.send('Dealguy is ON and in morale boost mode.');
  setTimeout(function(){
    var process = childProc.spawn('python',["/home/pi/dealguy/theguy.py", "morale_boost"]);
    console.log('Deal guy is running in morale boost mode.');
    process.stdout.on('data', function (data){
      console.log(data.toString());
    });
  }, 1);
});

app.listen(3000, function () {
  console.log('Dealguy app listening on port 3000!');
});
