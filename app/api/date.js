// serve the current date
const date = new Date();

exports.today = (req, res) => {
    res.json({
        year: date.getUTCFullYear(),
        month: date.getUTCMonth() + 1,
        day: date.getUTCDate()
    });
};
