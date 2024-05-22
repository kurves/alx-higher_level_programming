#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Check if movie ID is provided
if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

// Construct the API URL
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the API
request(url, (error, response, body) => {
  if (error) {
    console.error('Error making the request:', error);
    return;
  }

  // Parse the response body as JSON
  const data = JSON.parse(body);

  // Check if the movie exists
  if (response.statusCode === 200) {
    // Print the title of the movie
    console.log(data.title);
  } else {
    console.error('Movie not found');
  }
});
