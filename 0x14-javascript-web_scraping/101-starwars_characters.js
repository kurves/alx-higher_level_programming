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
  const fetchCharacter = (url, callback) => {
    request(url, (err, response, body) => {
      if (err) {
        callback(err);
        return;
      }
      if (response.statusCode !== 200) {
        callback(new Error('Failed to fetch character'));
        return;
      }
      callback(null, JSON.parse(body).name);
    });
  };
  const fetchAllCharacters = (index) => {
    if (index >= characters.length) {
      return;
    }
    fetchCharacter(characters[index], (err, name) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(name);
      fetchAllCharacters(index + 1);
    });
  };
  fetchAllCharacters(0);
});
