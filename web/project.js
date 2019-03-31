var arcs = new Datamap({
    element: document.getElementById("container"),
    scope: 'world',
});

// Arcs coordinates can be specified explicitly with latitude/longtitude,
// or just the geographic center of the state/country.
arcs.arc([
    {
        origin: {
            latitude: 40.639722,
            longitude: -73.778889
        },
        destination: {
            latitude: 5.660759,
            longitude: -66.055238
        }
    },
    {
        origin: {
            latitude: 40,
            longitude: 111
        },
        destination: {
            latitude: 25.793333,
            longitude: -80.290556
        },
        options: {
            strokeWidth: 5,
            strokeColor: 'rgba(100, 10, 200, 0.4)',
            greatArc: true
        }
    },
    {
        origin: {
            latitude: 39.861667,
            longitude: -104.673056
        },
        destination: {
            latitude: 39.857420,
            longitude: 126.798484
        }
    }
], { strokeWidth: 5, arcSharpness: 1.4 });