const express = require('express');
const axios = require('axios');
const path = require('path');
const amulet = require('./amulet');
const daas = require('./daas');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => {
    res.sendFile('api-test.html', { root: path.join(__dirname, './pages') });
});

app.post('/move', async (req, res) => {
    l = amulet.parse_move(req.body);
    if(Object.keys(l).length === 0){
        res.status(400).send('Invalid input move format');
        return;
    }
    r = await daas.get_response(l);
    res.send(r);
});

app.listen(port, () => console.log(`Listening on port ${port}...`));
