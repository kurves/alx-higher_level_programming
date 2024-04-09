#!/usr/bin/node

exports.callMeXTimes = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
