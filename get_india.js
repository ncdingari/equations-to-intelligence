const https = require('https');
https.get('https://raw.githubusercontent.com/johan/world.geo.json/master/countries/IND.geo.json', (res) => {
    let rawData = '';
    res.on('data', (chunk) => { rawData += chunk; });
    res.on('end', () => {
        try {
            const parsedData = JSON.parse(rawData);
            let coords = parsedData.features[0].geometry.coordinates;
            // flatten arrays
            console.log(JSON.stringify(coords[0]));
        } catch (e) { console.error(e.message); }
    });
});
