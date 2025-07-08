#!/usr/bin/node
const { argv } = require('node:process');

const a = parseInt(argv[2]);
const b = parseInt(argv[3]);

console.log(a + b);
