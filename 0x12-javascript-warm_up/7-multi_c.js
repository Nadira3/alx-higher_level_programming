#!/usr/bin/node
let x = process.argv[2];
if (x === undefined) { console.log('Missing number of occurrences'); } else {
  const myVar = 'C is fun';
  while (x > 0) {
    console.log(myVar);
    x--;
  }
}
