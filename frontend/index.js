const express = require('express');
//const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();


//app.set('view engine', 'ejs');

//app.use(bodyParser.urlencoded({ extended: false }));

// Connect to MongoDB
//no local host as the docker image thus the containerwill (probably) 
//retrieved from the docker page
/*
mongoose
  .connect(
    'mongodb://mongo:27017/docker-node-mongo',
    { useNewUrlParser: true }
  )
  .then(() => console.log('MongoDB Connected'))
  .catch(err => console.log(err));

const Item = require('./models/Item');

//start with two routes, home page
//ADD MORE ROUTES IF NECESSARY
app.get('/', (req, res) => {
  Item.find()
    .then(items => res.render('index', { items }))
    .catch(err => res.status(404).json({ msg: 'No items found' }));
});

app.post('/item/add', (req, res) => {
  const newItem = new Item({
    name: req.body.name
  });

  newItem.save().then(item => res.redirect('/'));
});
*/
//THIS PORT has to be passed on to the Dockerfile
// to run it later from any custom port
//var port = process.env.PORT || 3000;

const port =  3000;


app.listen(port, () => console.log('Server running on port ' + port));
//app.listen(3000, function () {
//  console.log('Example app listening on port ' + port + '!');
//});