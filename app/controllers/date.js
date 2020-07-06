exports.renderPage = (req, res) => {
    res.render('date', {ip: req.ip});
}