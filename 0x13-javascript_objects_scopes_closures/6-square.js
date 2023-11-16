#!/usr/bin/node

const oldSquare = require('./5-square.js');

class Square extends oldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (ch) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (ch != null) { process.stdout.write(ch); } else { process.stdout.write('X'); }
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Square;
