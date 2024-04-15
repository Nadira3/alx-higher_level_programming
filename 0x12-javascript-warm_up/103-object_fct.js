#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

// Define the incr function
myObject.incr = function () {
  this.value += 1; // Increment the value property by 1
};

// Call the incr function and log the updated object
myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
