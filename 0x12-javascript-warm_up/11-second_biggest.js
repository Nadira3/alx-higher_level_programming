#!/usr/bin/node
const argArray = process.argv;
let numList = [];

for (arg of argArray) {
	if (!isNaN(arg))
		numList.push(arg);
}
secLargest = numList.sort((a, b) => (a - b))[numList.length - 2];
if (secLargest === undefined)
	console.log(0);
else
	console.log(secLargest);
