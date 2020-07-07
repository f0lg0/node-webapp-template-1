const inquirer = require('inquirer');
const fs = require('fs');

const QUESTIONS = [
  {
    name: 'name',
    type: 'input',
    message: 'Project name:'
  },
  {
    name: 'description',
    type: 'input',
    message: 'Project description:'
  },
  {
    name: 'author',
    type: 'input',
    message: 'Author:'
  }
];


inquirer.prompt(QUESTIONS)
  .then(answers => {
    const name = answers['name'];
    const description = answers['description'];
    const author = answers['author'];

    // this is based on the simple-node-webapp template
    const appDetails =  {
        name: name,
        version: "1.0.0",
        description: description,
        main: "server.js",
        scripts: {
            start: "node server.js",
            dev: "nodemon server.js"
        },
        author: author,
        license: "MIT",
        dependencies: {
            "cookie-parser": "^1.4.5",
            "dotenv": "^8.2.0",
            "ejs": "^3.1.3",
            "express": "^4.17.1",
            "helmet": "^3.23.3",
            "jsonwebtoken": "^8.5.1",
            "mongoose": "^5.9.21",
            "morgan": "^1.10.0"
        },
        devDependencies: {
            "nodemon": "^2.0.4"
        }
    }

    const packagejson = JSON.stringify(appDetails);

    // creating project directory
    console.log("[CREATING] Project folder")
    fs.mkdirSync(name);
    console.log("[*] Done")


    // writing packagejson
    console.log("[WRITING] package.json")
    fs.writeFileSync(`${name}/package.json`, packagejson, 'utf-8');
    console.log("[*] Done")

});
