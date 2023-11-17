#!/usr/bin/node
const firstArg = process.argv[2];
const argNum = parseInt(firstArg);
if (firstArg === undefined || isNaN(argNum)) { console.log('Not a number'); } else { console.log("My number: " + argNum); }
