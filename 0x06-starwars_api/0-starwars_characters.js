#!/usr/bin/node
/**
 * Write a script that prints all characters of a Star Wars movie:
 * - The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
 * - Display one character name per line in the same order as the “characters” list in the /films/ endpoint
 * - You must use the Star wars API
 * - You must use the request module
 */

const request = require('request');

const fetch = (url) => new Promise((resolve, reject) => {
  request(url, (err, _, body) => {
    if (err) reject(err);
    else resolve(JSON.parse(body));
  });
});

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./star_wars_characters.js <movie_id>');
  process.exit(1);
}

fetch(`https://swapi.dev/api/films/${movieId}/`)
  .then(film => Promise.all(film.characters.map(fetch)))
  .then(characters => characters.forEach(character => console.log(character.name)))
  .catch(console.error);
