#!/usr/bin/node
let firstArg = process.argv[2];
let secArg = process.argv[3];
if (firstArg === null) { firstArg = 'undefined'; }
if (secArg === null) { secArg = 'undefined'; }
console.log(firstArg + ' is ' + secArg);
