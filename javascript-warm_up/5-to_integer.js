#!/usr/bin/node
const { argv } = require('node:process');

if (isNaN(parseInt(argv[2]))) {
  console.log('Not a number');
} else {
  console.log(parseInt(argv[2]));
}
