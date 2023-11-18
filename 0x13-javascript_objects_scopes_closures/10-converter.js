#!/usr/bin/node

class BaseObject {
  constructor (base) {
    this.base = base;
  }
}

exports.converter = function (base) {
  const baseObject = new BaseObject(base);

  function convert (base) {
    return base.toString(baseObject.base);
  }

  return convert;
};
