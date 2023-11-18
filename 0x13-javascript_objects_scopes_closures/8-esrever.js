#!/usr/bin/node

// function that reverses a list
exports.esrever = function (list) {
  const revList = [];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) { revList[i] = list[j]; }
  return revList;
};
