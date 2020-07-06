
const express = require('express');
const router = express.Router();

const date = require('../api/date.js');

router.get('/date', date.today);

module.exports = router