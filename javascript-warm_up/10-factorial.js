#!/usr/bin/node
const { argv } = require('node:process');

function factorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const a = parseInt(argv[2]);
if (isNaN(a)) {
  console.log('1');
}
result = factorial(a);
console.log(result);
