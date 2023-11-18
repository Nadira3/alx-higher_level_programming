#!/usr/bin/node

const oldList = require('./100-data.js')['list'];
console.log(oldList);

newList = oldList.map((x) => x * oldList.indexOf(x));
console.log(newList);
