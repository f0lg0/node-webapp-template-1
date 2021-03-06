# node-webapp-template-1
A really simple NodeJS webapp template (REST API) structured by dividing content by technical role. This is not recognized as a "best practice" but I find it easy to understand. 
Check out my other components structured template [HERE](https://github.com/f0lg0/node-webapp-template-2)

## Project Structure

* api
  * date.js
  * readme.md
* config
  * readme.md
* controllers
  * date.js
  * index.js
  * readme.md
* middlewares
  * readme.md
* models
  * readme.md
* public
  * css
    * styles.css
  * images
    * readme.md
  * javascript
    * switchTheme.js
    * fetchDate.js
  * 404.html
  * index.html
  * readme.md
* routes
  * api.js
  * date.js
  * index.js
  * readme.md
* views
  * date.ejs
  * readme.md
* wireframes
  * readme.md
* package-lock.json
* package.json
* server.js


## npm Packages

* cookie-parser
* dotenv
* ejs
* express
* helmet
* jsonwebtoken
* mongoose
* morgan
* nodemon

### Run

```
npm install .
```

```
npm run dev
```

## Project Generator

MOVED PROJECT GENERATOR [HERE](https://github.com/f0lg0/snpgen)

There's a project generator written in Python and Javascript to generate everything you need without an Internet connection. It generates the same project template of this directory so you can get the same content even if you don't have the option to clone this repo. 

#### Other Info

For more informations about the template check the readme.md inside every folder.

