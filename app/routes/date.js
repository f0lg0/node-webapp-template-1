const express = require('express');
const router = express.Router();

const date = require('../controllers/date.js');

router.get('/', date.renderPage);

module.exports = router