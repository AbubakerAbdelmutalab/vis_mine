var map = new Datamap({
    element: document.getElementById("container"),
    scope: 'world',
});
var data = JSON.parse(data); //import the data
var arcs = []
var i = 0;
//create the array of arcs using 300 data points
while (arcs.length < 300) {
    if (isNaN(data[i].latitude)) {
        i++;
        continue;
    }
    arc = {
        origin: {
            latitude: data[i].latitude,
            longitude: data[i].longitude
        },
        //dont have real destinations yet so all will go to utah
        destination: {
            latitude: 40.767584,
            longitude: -111.844630
        }
    }
    //color the arc line based on the login type
    switch (data[i].type) {
        case "INVALID_USER":
            arc.options = {
                strokeWidth: 2,
                strokeColor: 'red',
                greatArc: true
            };
            break;
        case "FAILED_PASSWORD":
            arc.options = {
                strokeWidth: 2,
                strokeColor: 'yellow',
                greatArc: true
            };
        default:
            arc.options = {
                strokeWidth: 2,
                strokeColor: 'green',
                greatArc: true
            };
    }
    arcs.push(arc);
    i++;
}
map.arc(arcs, { strokeWidth: 2, arcSharpness: 1.4 });