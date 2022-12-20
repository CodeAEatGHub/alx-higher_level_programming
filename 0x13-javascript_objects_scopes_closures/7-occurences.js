#!/usr/bin/node
// Counts number of occurences of an element in a list
exports.nbOccurences = function (list, element) {
  return list.filter(x => x === element).length;
};