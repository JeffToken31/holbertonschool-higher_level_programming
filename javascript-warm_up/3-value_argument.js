#!/usr/bin/node
const { argv } = require('node:process');

if (argv[2] === undefined) {
  console.log('No argument');
} else {
  for (const element of argv.slice(2)) {
    console.log(element);
  }
}
