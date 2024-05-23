#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, { json: true }, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error('An error occurred. Status code:', response.statusCode);
    return;
  }
  
  const tasksCompleted = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
