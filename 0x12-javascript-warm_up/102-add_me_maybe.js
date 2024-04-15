#!/usr/bin/node
function addMeMaybe(number, theFunction) {
    number += 1; // Increment the input number
    theFunction(number); // Call the function with the incremented number
}

// Export the function so that it can be used in other modules/files
module.exports = {
    addMeMaybe: addMeMaybe
};

