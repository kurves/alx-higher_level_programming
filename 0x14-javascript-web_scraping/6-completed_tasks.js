#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
  console.error('Usage: ./script.js <API_URL>');
  process.exit(1);
}

request(url, function (err, response, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error('An error occurred. Status code:', response.statusCode);
    return;
  }
  
  const tasks = JSON.parse(body);
  const completedTasksByUser = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (!completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId] = 0;
      }
      completedTasksByUser[task.userId]++;
    }
  });

  for (const userId in completedTasksByUser) {
    console.log(`'${userId}': ${completedTasksByUser[userId]}`);
  }
});

