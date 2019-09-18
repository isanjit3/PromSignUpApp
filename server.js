//Add different dependencies and modules
const express    = require('express');
const path       = require('path');
const app        = express();
const bodyParser = require('body-parser');
const fileUpload = require('express-fileupload');
const csvtojson  = require('csvtojson');
const firebase   = require('firebase');
const replace    = require('replace');

//Initialize Firebase
var firebaseConfig = {
  apiKey: "AIzaSyCCgoy1_bJzrruepLYIWBbrIUIGxM-p2CQ",
  authDomain: "signup-form-e4c78.firebaseapp.com",
  databaseURL: "https://signup-form-e4c78.firebaseio.com",
  projectId: "signup-form-e4c78",
  storageBucket: "signup-form-e4c78.appspot.com",
  messagingSenderId: "1000336889334",
  appId: "1:1000336889334:web:f5099e3a8ecc1584"
};
firebase.initializeApp(firebaseConfig);

//Write data to Firebase
function writeFirebase(jsonData, collection) {
  var database = firebase.database();
  var ref = firebase.database().ref(collection);

  jsonData.forEach(item => {
    item.FULLNAME = item.FIRST + ' ' + item.LAST;
    ref.child(item.ID).set(item);
  });
}

//Read data from Firebase
function readFirebaseTickets() {
  return firebase.database().ref('tickets').once('value').then(function (snapshot) {
    var jsonData = [];
    snapshot.forEach(function (child) {

      var info = {
        "first": child.child("first").val(),
        "middle": child.child("middle").val(),
        "last": child.child("last").val(),
        "sID": child.child("sID").val(),
        "ticket": child.key,
        "grade": child.child("grade").val(),
        "guestBool": child.child("guestBool").val(),
        "guest": child.child("guest").val()
      }
      jsonData.push(info);

    });
    return jsonData;
  });
}

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '/views'));
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(fileUpload());

//Render main page
app.get('/', function (req, res) {
  res.render('index');
})

//Render main page
app.get('/index', function (req, res) {
  res.render('index');
})

//Render the search student page
app.get('/search-student', function (req, res) {
  res.render('search-student', {
    fbConfig: firebaseConfig
  });
})

//Render the ticket entry page
app.get('/ticket-entry', function (req, res) {
  res.render('ticket-entry');
})

//Render the upload files page
app.get('/upload', function (req, res) {
  res.render('upload');
})

//Render uploads page with status messages
app.post('/upload', function (req, res) {
  if (!req.files || Object.keys(req.files).length == 0) {
    return res.render('msg', {
      msg: 'Please choose a file to upload',
      styleClass: 'alert-danger',
      status: 'error'
    });
  }

  // The name of the input field (i.e. "sampleFile") is used to retrieve the uploaded file
  let csvFile = req.files.csvFile;
  let collectionName = req.body.collectionName;
  let str = csvFile.data.toString('utf8');
  console.log(str)

  csvtojson().fromString(str).then(jsonData => {
    //console.log(jsonData);
    writeFirebase(jsonData, collectionName);
  });

  res.render('msg', {
    msg: 'Your file has been uploaded.',
    styleClass: 'alert-success',
    status: 'success'
  });
})

//Render the display tickets page
app.get('/display-ticket-data', function (req, res) {
  readFirebaseTickets().then(function (data) {
    //console.log(data)
    res.render('display-ticket-data',
      {
        studentsData: data
      }
    );
  })
})

//Render the settings page
app.get('/settings', function (req, res) {
  res.render('settings');
})

//Render the help page
app.get('/help', function (req, res) {
  res.render('help');
})

//Listen for web application on Localhost:3000
app.listen(8000, function () {
  console.log('Example app listening on port 3000!')
})