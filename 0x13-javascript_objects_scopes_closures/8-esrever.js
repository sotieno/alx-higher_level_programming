#!/usr/bin/node
// reverses a list
exports.esrever = function (list) {
  for (let index = 0; index < parseInt(list.length / 2); index++) {
    const tmp = list[list.length - 1 - index];
    list[list.length - 1 - index] = list[index];
    list[index] = tmp;
  }
  return list;
};
