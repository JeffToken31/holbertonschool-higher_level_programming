#!/usr/bin/node
const { argv } = require('node:process');

let i = 0;
const number = parseInt(argv[2]);

if (isNaN(number)) {
  console.log('Missing number of occurrences');
}
while (i < number) {
  console.log('C is fun');
  i++;
}
