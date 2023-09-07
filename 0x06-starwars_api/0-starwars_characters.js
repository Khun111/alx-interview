request = require('request');

film = request(`https://swapi.dev/api/films/${process.argv[1]}`);

console.log(film);
