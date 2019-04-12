function getBubbles(types,section) {
	var i = (section-1)*(data.length/10)
	var max = (section)*(data.length/10)
	var countryCount = new Map()
	while (i < section) {
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
        radius: 5*Math.log(value.count) + value.count*.1/Math.log(value.count), //increase the radius of the bubble for every login attempt by the country
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