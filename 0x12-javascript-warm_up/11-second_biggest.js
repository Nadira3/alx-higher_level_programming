#!/usr/bin/node
const argArray = process.argv;
const numList = [];
let arg;

for (arg of argArray) {
  if (!isNaN(arg)) { numList.push(arg); }
}
const secLargest = numList.sort((a, b) => (a - b))[numList.length - 2];
if (secLargest === undefined) { console.log(0); } else { console.log(secLargest); }
