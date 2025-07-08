#!/usr/bin/node
const { parse } = require('node:path');
const { argv } = require('node:process');

let a = parseInt(argv[2]);
let b = parseInt(argv[3]);

console.log(a + b);
