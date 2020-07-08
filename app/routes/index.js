const express = require('express');
const router = express.Router();

const home = require('../controllers/index.js');

router.get('/', home.homePage);

module.exports = router;
