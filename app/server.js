const express = require('express');
const app = express();

require('dotenv').config()

const morgan = require('morgan');
const path = require('path');
const helmet = require("helmet");
const mongoose = require('mongoose');
const cookieParser = require('cookie-parser');

app.use(express.static('public'));
app.use(express.urlencoded({ extended: false }))
app.set('view engine', 'ejs');

// Middlewares
app.use(morgan('dev')); // change to common for production
app.use(helmet()); // secure headers
app.use(cookieParser()); // cookies

// Mongo URI
mongoose.set('useNewUrlParser', true);
mongoose.set('useFindAndModify', false);
mongoose.set('useCreateIndex', true);


const mongoURI = process.env.DB_URI || 'mongodb://localhost/db-name';
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });

const db = mongoose.connection;
db.on('error', error => console.error(error));
db.once('open', () => console.log(`Connected to database [${mongoURI}]`));

const home = require('./routes/index.js');
const api = require('./routes/api.js');

const date = require('./routes/date.js');

app.use('/', home);
app.use('/api', api);

app.use('/today', date);

/* HANDLING 404 ERRORS */
app.use((req, res) => {
    res.status(404);
    res.sendFile(path.join(__dirname + '/public/404.html'));
});

const host = process.env.HOST || "localhost";
const port = process.env.PORT || 5000;

app.listen(port, host, () => {
    console.log(`Server running at http://${host}:${port}`);
});