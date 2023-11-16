#!/usr/bin/node
const firstArg = parseInt(process.argv[2]);
const secArg = parseInt(process.argv[3]);

function add (a, b) { return a + b; }

console.log(add(firstArg, secArg));
