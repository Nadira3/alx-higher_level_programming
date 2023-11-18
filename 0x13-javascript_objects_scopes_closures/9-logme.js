#!/usr/bin/node

class SaveLog {
  constructor () {
    this.staticCount = -1;
  }

  incr () {
    this.staticCount += 1;
    return this.staticCount;
  }
}
const count = new SaveLog();

// function that saves log staticCount
exports.logMe = function (item) {
  console.log(count.incr() + ': ' + item);
};
