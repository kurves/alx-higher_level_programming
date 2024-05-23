#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error('An error occurred. Status code:', response.statusCode);
    return;
  }
  
  const filmData = JSON.parse(body);
  const characters = filmData.characters;
  
  characters.forEach(characterUrl => {
    request(characterUrl, function (err, response, body) {
      if (err) {
        console.error(err);
        return;
      }
      
      if (response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      } else {
        console.error('An error occurred. Status code:', response.statusCode);
      }
    });
  });
});

