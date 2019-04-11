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
var countryCount = new Map();
var i = 0;
//count login attempt by country using 3000 data points
while (i < 3000) {
    //skip if country is not known
    if (data[i].country == "UNKNOWN") {
        i++;
        continue;
    }
    //if country is not yet mapped, create a new entry
    if (countryCount.get(data[i].country) == null) {
        countryCount.set(data[i].country, { count: 0, latitude: data[i].latitude, longitude: data[i].longitude });
    }
    //increment the count and add to map
    let countryStuff = countryCount.get(data[i].country)
    countryStuff.count++;
    countryCount.set(data[i].country, countryStuff);
    i++;
}
//create a bubble for each country in the map
var bubbles = [];
countryCount.forEach(function (value, key) {
    bubble = {
        radius: 5 + (value.count*.1), //increase the radius of the bubble for every login attempt by the country
        loginAttempts: value.count,
        country: key,
        latitude: value.latitude,
        longitude: value.longitude,
        fillKey: 'red',
    }
    bubbles.push(bubble);
});
//sort the bubbles so biggest bubbles will be on the bottom
bubbles.sort((a, b) => { return b.loginAttempts - a.loginAttempts});
//add the bubbles to the map and give it a hover display
map.bubbles(bubbles, {
    popupTemplate: function (geo, data) {
        return '<div class="hoverinfo">Login Attempts:' + data.loginAttempts + ' by ' + data.country + ''
    }
});