#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length < 4) {
  console.log('undefined is undefined');
} else {
  console.log(''.concat(argv[3], ' is ', argv[4]));
}
