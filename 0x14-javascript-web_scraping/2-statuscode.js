#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.error('Please provide a URL as the first argument.');
  process.exit(1);
}

request(url, (error, response) => {
  if (error) {
    console.error('Error making the request:', error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
