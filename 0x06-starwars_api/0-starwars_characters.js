#!/usr/bin/node
/**
 * Write a script that prints all characters of a Star Wars movie:
 * - The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
 * - Display one character name per line in the same order as the “characters” list in the /films/ endpoint
 * - You must use the Star Wars API
 * - You must use the request module
 */

const request = require('request'); // Import the request module
const movieId = process.argv[2];    // Get the Movie ID from command-line arguments

if (!movieId) {
  console.error('Usage: ./star_wars_characters.js <movie_id>'); // Print usage if no Movie ID
  process.exit(1); // Exit with error code
}

const url = `https://swapi.dev/api/films/${movieId}/`; // SWAPI URL for the given Movie ID

// Fetch movie details
request(url, (error, response, body) => {
  if (error) return console.error(error); // Handle error

  const film = JSON.parse(body); // Parse the JSON response
  const characters = film.characters; // Get the list of character URLs

  // Fetch each character's details
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) return console.error(error); // Handle error
      const character = JSON.parse(body); // Parse the JSON response
      console.log(character.name); // Print the character's name
    });
  });
});
