# node-webapp-template
A really simple NodeJS webapp template (REST API) + Offline project generator

# DISCLAIMER
Tomorrow I will move the project generator to a new repo to keep everything more organized.
Stay tuned.

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

There's a project generator written in Python to generate everything you need without an Internet connection. It generates the same project template of this directory so you can get the same content even if you don't have the option to clone this repo. 

Why Python? Just because I am comfortable with it and it does the job (it is also fast).

### Run

```
python3 generate.py
```

Just run this file and you will be go to go, it even install all the depndencies from the package.json file.

The project template is taken from the template file, there you will find all the files and their relative content.

Have fun with it and customize it as you like! If you tweak it, it can be used to generate other projects too!

### Note

The files are one-line pieces of code, you may want to beautify them.



## Coming soon

- [ ] Project Generator written in Javascript (NodeJS)



#### Other Info

For more informations about the template check the readme.md inside every folder.

