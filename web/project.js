var map = new Datamap({
    element: document.getElementById("container"),
    scope: 'world',
    geographyConfig: {
        popupOnHover: false,
        highlightOnHover: false
    },
    fills: {
        defaultFill: '#ABDDA4',
        blue: 'blue',
        red: 'red'
    }
});
var data = JSON.parse(data); //import the data included in the html file
var slider = document.getElementById("myRange");
// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    boxChecked();
}
function boxChecked() {
    map.bubbles([]);
    var types = ["INVALID_USER", "FAILED_PASSWORD", "DISCONNECT", "DISCONNECT_INVALID_USER", "ACCEPT_PUBLIC_KEY", "DISCONNECT_PREAUTH", "REVERSE_MAPPING", "TOO_MANY_PASSWORD_ATTEMPTS", "UNABLE_TO_NEGOTIATE", "NEW_SESSION", "REMOVE_SESSION", "NO_IDENTIFICATION"];
    var checkboxes = [];
    types.forEach((type) => {
        checkboxes.push(document.getElementById(type));
    });
    var checked = [];
    checkboxes.forEach((box, index) => {
        if(box.checked == true){
            checked.push(types[index]);
        }
    });
    var bubbles = getBubbles(checked, slider.value);
    bubbles = bubbles.sort((a, b) => { return b.loginAttempts - a.loginAttempts });
    map.bubbles(bubbles, {
        popupTemplate: function (geo, data) {
            return '<div class="hoverinfo">Login Attempts:' + data.loginAttempts + ' by ' + data.country + ''
        }
    });
}

function getBubbles(types,section) {
	var i = Math.floor((section-1)*(data.length/10));
    var max = Math.floor(i + (data.length/10));
	var countryCount = new Map()
	while (i < max) {
		var msg = data[i]
		if (types.indexOf(msg.type) >= 0 && !(msg.country === "UNKNOWN")) {
			//if country is not yet mapped, create a new entry
		    if (countryCount.get(data[i].country) == null) {
		        countryCount.set(data[i].country, { count: 0, latitude: data[i].latitude, longitude: data[i].longitude });
		    }
		    //increment the count and add to map
		    let countryStuff = countryCount.get(data[i].country)
		    countryStuff.count++;
		    countryCount.set(data[i].country, countryStuff);
		}
		i++
	}

	var bubbles = [];
	countryCount.forEach(function (value, key) {
    bubble = {
        radius: 5+value.count*.1, //increase the radius of the bubble for every login attempt by the country
        loginAttempts: value.count,
        country: key,
        latitude: value.latitude,
        longitude: value.longitude,
        fillKey: 'red',
    }
    bubbles.push(bubble);
	});
	return bubbles
}