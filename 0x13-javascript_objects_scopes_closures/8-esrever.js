#!/usr/bin/node
// reverses a list
exports.esrever = function (list) {
  return list.sort((a, b) => b - a);
};
