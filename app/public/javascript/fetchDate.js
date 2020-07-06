const API_URL = 'http://localhost:5000/api/date';

fetch(API_URL)
.then(res => res.json())
.then((result) => {
	if (result) {
		document.getElementById('fetched-date').innerHTML = result.year + "/" + result.month + "/" + result.day;
	} else {
		document.getElementById('fetched-date').innerHTML = "Ooops! Error fetching the API";
	}
});