#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error', error);
    return;
  }

  const data = JSON.parse(body);

  if (response.statusCode === 200) {
    console.log(data.title);
  } else {
    console.error('Movie not found');
  }
});
