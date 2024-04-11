#!/usr/bin/node
const { dict } = require('./101-data');

const usersByOccurrence = {};

for (const [userId, occurrence] of Object.entries(dict)) {
    if (occurrence in usersByOccurrence) {
        usersByOccurrence[occurrence].push(parseInt(userId));
    } else {
        usersByOccurrence[occurrence] = [parseInt(userId)];
    }
}

console.log(usersByOccurrence);
