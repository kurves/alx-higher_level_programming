#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the API URL as the first argument.');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error making the request:', error);
    return;
  }

  const todos = JSON.parse(body);

  const completedTasksByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId] = 0;
      }
      completedTasksByUser[todo.userId]++;
    }
  });

  for (const userId in completedTasksByUser) {
    console.log(`User ${userId} has completed ${completedTasksByUser[userId]} tasks`);
  }
});
