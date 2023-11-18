#!/usr/bin/node

exports.converter = function (base) {

  function convert (numBase) {
    return numBase.toString(base);
  }

  return convert;
};
