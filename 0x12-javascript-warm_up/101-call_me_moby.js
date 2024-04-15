#!/usr/bin/node
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

// Export the function so that it can be used in other modules/files
module.exports = {
  callMeMoby
};
