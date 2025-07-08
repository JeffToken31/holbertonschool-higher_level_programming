#!/usr/bin/node
const { argv } = require('node:process');

let i = 0;
let j = 0;
let row = '';
const number = parseInt(argv[2]);

if (isNaN(number)) {
  console.log('Missing size');
}

while (i < number) {
  while (j < number) {
    row += 'X';
    j++;
  }
  console.log(row);
  i++;
}
