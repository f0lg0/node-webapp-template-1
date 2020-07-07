entryPoint = {
    'server.js' : "const express = require('express'); const app = express(); require('dotenv').config(); const morgan = require('morgan'); const path = require('path'); const helmet = require('helmet'); const mongoose = require('mongoose'); const cookieParser = require('cookie-parser'); app.use(express.static('public')); app.use(express.urlencoded({ extended: false })); app.set('view engine', 'ejs'); app.use(morgan('dev')); app.use(helmet()); app.use(cookieParser()); mongoose.set('useNewUrlParser', true); mongoose.set('useFindAndModify', false); mongoose.set('useCreateIndex', true); const mongoURI = process.env.DB_URI || 'mongodb://localhost/db-name'; mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true }); const db = mongoose.connection; db.on('error', error => console.error(error)); db.once('open', () => console.log(`Connected to database [${mongoURI}]`)); const home = require('./routes/index.js'); const api = require('./routes/api.js'); const date = require('./routes/date.js'); app.use('/', home); app.use('/api', api); app.use('/today', date); app.use((req, res) => { res.status(404); res.sendFile(path.join(__dirname + '/public/404.html')); }); const host = process.env.HOST || 'localhost'; const port = process.env.PORT || 5000; app.listen(port, host, () => { console.log(`Server running at http://${host}:${port}`); });"
}

package = {
    "name": "webapp-template",
    "version": "1.0.0",
    "description": "A really simple Nodejs webapp template",
    "main": "server.js",
    "scripts": {
        "start": "node server.js",
        "dev": "nodemon server.js"
    },
    "repository": {
        "type": "git",
        "url": "git+https://github.com/f0lg0/node-webapp-template.git"
    },
    "author": "Leonardo Folgoni",
    "license": "MIT",
    "bugs": {
        "url": "https://github.com/f0lg0/node-webapp-template/issues"
    },
    "homepage": "https://github.com/f0lg0/node-webapp-template#readme",
    "dependencies": {
        "cookie-parser": "^1.4.5",
        "dotenv": "^8.2.0",
        "ejs": "^3.1.3",
        "express": "^4.17.1",
        "helmet": "^3.23.3",
        "jsonwebtoken": "^8.5.1",
        "mongoose": "^5.9.21",
        "morgan": "^1.10.0"
    },
    "devDependencies": {
        "nodemon": "^2.0.4"
    }
}

folders = {
    'api' : None, 
    'config' : None,
    'controllers' : None, 
    'middlewares' : None, 
    'models' : None, 
    'public' : ['css', 'images', 'javascript'], 
    'routes' : None, 
    'views' : None, 
    'wireframes' : None
}

readmes = {
    'api' : 'files related to the API, like auth logic files. I usually make APIs that respond with JSON data. No web views.',
    'config' : 'all configuration files and nothing else',
    'controllers' : 'all the logic needed to the routes and nothing else',
    'middlewares' : 'all those functions that you want to run in the middle of another process. For example a middleware that checks for a valid JWT token in every request.',
    'models' : 'all the db models (MongoDB - Mongoose) files and nothing else',
    'public' : 'all the public files and nothing else',
    'routes' : 'all the routes (to handle reqs) files and nothing else',
    'views' : 'here we should place all the server side rendered pages and nothing else',
    'wireframes' : 'all the designs, prototypes, mockups etc'
}

appFiles = {
    'api' : {'date.js' : "const date = new Date(); exports.today = (req, res) => { res.json({ year: date.getUTCFullYear(), month: date.getUTCMonth() + 1, day: date.getUTCDate() }); }"},
    'controllers' : {
        'date.js' : "exports.renderPage = (req, res) => { res.render('date', {ip: req.ip}); }",
        'index.js' : "exports.homePage = (req, res) => { res.sendFile('/index.html'); }"
    },

    'public' : {
        '404.html' : '<!DOCTYPE html> <html> <head> <title>Not found</title> <link rel="stylesheet" type="text/css" href="./css/styles.css"> <link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@300&display=swap" rel="stylesheet"> </head> <body> <script src="javascript/switchTheme.js"></script> <div class="errorBanner"> <h1>Error</h1> <hr class="hr-style-two"> <p>404 Not Found</p> </div> </body> </html>',
        'index.html' : '<!DOCTYPE html> <html> <head> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1" /> <title>Home</title> <link rel="stylesheet" type="text/css" href="./css/styles.css"> <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap" rel="stylesheet"> </head> <body> <script src="javascript/switchTheme.js"></script> <div class="logo"> <h1>Home</h1> </div> <div class="action"> <form action="/today"> <input type="submit" value="Get Date"> </form> </div> <div class="action"> <input type="submit" value="Switch Theme" onclick="toggleTheme()"> </div> </body>'
    },

    'public/css' : {
        'styles.css' : ".light-theme { --color-primary: #FFF; --color-secondary: #EAEAEA; --color-tertiary: #666; --color-quaternary: #FAFAFA; --main-font-color: #000; --main-font-color-hr: rgba(0, 0, 0, 0.75); --secondary-font-color-hr: rgba(0, 0, 0, 0); } .dark-theme { --color-primary: #000; --color-secondary: #212121; --color-tertiary: #333; --color-quaternary: #111; --main-font-color: #FAFAFA; --main-font-color-hr: rgba(255, 255, 255, 0.75); --secondary-font-color-hr: rgba(255, 255, 255, 0); } body { font-family: 'Inter', sans-serif; background-color: var(--color-primary); } .logo { text-align: center; font-weight: 500; color: var(--main-font-color); } .errorBanner { position: absolute; width: 300px; height: 200px; z-index: 15; top: 50%; left: 50%; margin: -100px 0 0 -150px; text-align: center; color: var(--main-font-color); } .hr-style-two { margin-top: 20px; border: 0; height: 1px; width: 70%; background-image: linear-gradient(to right, var(--secondary-font-color-hr), var(--main-font-color-hr), var(--secondary-font-color-hr)); } .action{ margin: auto; width: 200px; } input[type=submit] { width: 100%; margin-bottom: 10px; background-color: var(--main-font-color); border: 1px solid var(--main-font-color); color: var(--color-primary); padding: 12px 20px; border-radius: 4px; cursor: pointer; transition: .3s; } input[type=submit]:hover { background-color: var(--color-primary); color: var(--main-font-color); border: 1px solid var(--main-font-color); border-radius: 4px; }"
    },

    'public/javascript' : {
        'fetchDate.js' : "const API_URL = 'http://localhost:5000/api/date'; fetch(API_URL) .then(res => res.json()) .then((result) => { if (result) { document.getElementById('fetched-date').innerHTML = result.year + '/' + result.month + '/' + result.day; } else { document.getElementById('fetched-date').innerHTML = 'Ooops! Error fetching the API'; } });",
        'switchTheme.js' : "function setTheme(themeName) { localStorage.setItem('theme', themeName); document.documentElement.className = themeName; } function toggleTheme() { if (localStorage.getItem('theme') === 'dark-theme') { setTheme('light-theme'); } else { setTheme('dark-theme'); } } (function() { if (localStorage.getItem('theme') === 'dark-theme') { setTheme('dark-theme'); } else { setTheme('light-theme'); } })();"
    },

    'routes' : {
        'api.js' : "const express = require('express'); const router = express.Router(); const date = require('../api/date.js'); router.get('/date', date.today); module.exports = router",
        'date.js' : "const express = require('express'); const router = express.Router(); const date = require('../controllers/date.js'); router.get('/', date.renderPage); module.exports = router",
        'index.js' : "const express = require('express'); const router = express.Router(); const home = require('../controllers/index.js'); router.get('/', home.homePage); module.exports = router"
    },

    'views' : {
        'date.ejs' : "<!DOCTYPE html> <html> <head> <title>Today</title> <link rel='stylesheet' type='text/css' href='./css/styles.css'> <link href='https://fonts.googleapis.com/css2?family=Ubuntu:wght@300&display=swap' rel='stylesheet'> </head> <body> <script src='javascript/switchTheme.js'></script> <% if (ip) { %> <div class='logo'> <p>Request IP: <%= ip %></p> </div> <% } %> <div class='logo'> <h2 id='fetched-date'></h2> </div> <script src='javascript/fetchDate.js'></script> </body> </html>"
    }

}