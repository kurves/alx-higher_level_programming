#!/usr/bin/node

exports.converter = function (base) {
  if (base === 10) {
    return arguments[1];
  } else {
    return parseInt(arguments[1]).toString(base);
  }
};
