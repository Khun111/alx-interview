request = require('request')

function fetchCharactersByIndex(characters, index) {
    if (index >= characters.length) process.exit(0)
    request(characters[index], (error, response, body) => {
        if (error || response.statusCode !== 200) console.log(error)
        actor = JSON.parse(body);
        console.log(actor.name)
        fetchCharactersByIndex(characters, index + 1)
    })
}
request(`https://swapi.dev/api/films/${process.argv[2]}`, (error, response, body) => {
    if (error || response.statusCode !== 200) console.log(error)
    film = JSON.parse(body);
    characters = film.characters
    fetchCharactersByIndex(characters, 0)
})



