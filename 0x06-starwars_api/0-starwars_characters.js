#!/usr/bin/node
/* Print star wars characters in order */
const request = require('request');

if (process.argv.length !== 3) process.exit(1);

function fetchCharactersByIndex (characters, index) {
  if (index >= characters.length) process.exit(0);
  request(characters[index], (error, response, body) => {
    if (error || response.statusCode !== 200) console.log(error);
    const actor = JSON.parse(body);
    console.log(actor.name);
    fetchCharactersByIndex(characters, index + 1);
  });
}
request(`https://swapi.dev/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error || response.statusCode !== 200) console.log(error);
  const film = JSON.parse(body);
  const characters = film.characters;
  fetchCharactersByIndex(characters, 0);
});
